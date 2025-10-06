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

    jd_file =request.files.get('jd_file')
    resume_files=request.files.getlist('resume_file')

    if not jd_file or not resume_files or jd_file.filename == '' or not resume_files[0].filename:
        return "Please upload one Job Description and at least one Resume.", 400

    jd_path = os.path.join(app.config['UPLOAD_FOLDER'], jd_file.filename)
    jd_file.save(jd_path)


    #traditional approach
    jd_info = parse_job_description(jd_path)
    if not jd_info["required_skills"]:
        os.remove(jd_path)
        return "Unable to extract required skills from job description", 500

    with open(jd_path, 'r', encoding='utf-8') as f:
        jd_text = f.read()
    os.remove(jd_path)
    all_candidate_results = []
    for resume_file in resume_files:
        if resume_file.filename == '':
            continue
        safe_filename=os.path.basename(resume_file.filename)
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
        resume_file.save(resume_path)


        resume_text = ""
        if resume_path.lower().endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume_path)
        elif resume_path.lower().endswith(".docx"):
            resume_text = extract_text_from_docx(resume_path)

        if not resume_text:

            os.remove(resume_path)
            all_candidate_results.append({
                'filename': resume_file.filename,
                'status': 'Failed to extract text.'
            })
            continue

        # Traditional Analysis
        contact_info = extract_contact_info(resume_text)
        candidate_skills = extract_skills(resume_text)
        match_score, matched_skills, missing_skills = calculate_match_score(candidate_skills, jd_info)

        # LLM Analysis
        llm_analysis = analyze_with_llm(resume_text, jd_text)

        candidate_result = {
            'filename': resume_file.filename,
            'status': 'Analysis Successful',
            'email': contact_info.get('email', 'N/A'),
            'phone': contact_info.get('phone', 'N/A'),
            'traditional_analysis': {
                'match_score': match_score,
                'skills_found': candidate_skills,
                'missing_skills': missing_skills,
            },
            'llm_analysis': llm_analysis if llm_analysis else {}
        }
        all_candidate_results.append(candidate_result)
        os.remove(resume_path)

    return render_template('batch_results.html', candidates=all_candidate_results)


if __name__ == '__main__':
    app.run(debug=True)