from flask import Flask, render_template, request
import os
import shutil
from dotenv import load_dotenv

from parser import extract_text_from_pdf, extract_text_from_docx
from extractor import extract_contact_info
from skills import extract_skills
from analyzer import parse_job_description, calculate_match_score
from llm_analyzer import analyze_with_llm

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = 'Resumes'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    if 'jd_file' not in request.files or 'resume_file' not in request.files:
        return "Files are not uploaded", 400

    jd_file = request.files['jd_file']
    resume_file = request.files['resume_file']

    if jd_file.filename == '' or resume_file.filename == '':
        return "File name is empty", 400

    jd_path = os.path.join(app.config['UPLOAD_FOLDER'], jd_file.filename)
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)

    jd_file.save(jd_path)
    resume_file.save(resume_path)

    #traditional approach
    jd_info = parse_job_description(jd_path)
    if not jd_info["required_skills"]:
        return "Unable to extract required skills from job description", 500

    resume_text = ""
    if resume_path.lower().endswith(".pdf"):
        resume_text = extract_text_from_pdf(resume_path)
    elif resume_path.lower().endswith(".docx"):
        resume_text = extract_text_from_docx(resume_path)

    if not resume_text:
        return f"Failed to extract text from this resume: {resume_file.filename}", 500

    contact_info = extract_contact_info(resume_text)
    candidate_skills = extract_skills(resume_text)
    match_score, matched_skills, missing_skills = calculate_match_score(candidate_skills, jd_info)

    #llm analysis approach
    with open(jd_path, 'r', encoding='utf-8') as f:
        jd_text = f.read()

    llm_analysis = analyze_with_llm(resume_text, jd_text)

    os.remove(jd_path)
    os.remove(resume_path)

    results = {
        'filename': resume_file.filename,
        'email': contact_info.get('email', 'Not Found'),
        'phone': contact_info.get('phone', 'Not Found'),
        'traditional_analysis': {
            'match_score': match_score,
            'skills_found': candidate_skills,
            'missing_skills': missing_skills,
        },
        'llm_analysis': llm_analysis if llm_analysis else {}
    }

    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)