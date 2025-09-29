import openai
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
load_dotenv()
def analyze_with_llm(resume_text, jd_text):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    prompt = f"""
    You are a professional resume analyst. Your task is to analyze a resume against a job description.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}

    Based on the documents above, provide a comprehensive analysis. Your response should be a JSON object with the following structure:
    {{
      "match_score": <int>,
      "summary_explanation": "<string, a one-paragraph summary of the match>",
      "strengths": ["<string, a key strength>", ...],
      "weaknesses": ["<string, a key weakness>", ...],
      "skills_matched": ["<string, a matched skill>", ...],
      "skills_missing": ["<string, a missing skill>", ...]
    }}

    The match_score should be a number from 0 to 100.
    The summary_explanation should be a single paragraph.
    The skills_matched and skills_missing lists should contain only skills directly from the job description.
    """

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')  # Or gemini-1.0-pro
        response = model.generate_content(prompt)

        if not response.text:
            print("Empty response.")
            return None

        analysis_json = response.text.strip()

        if analysis_json.startswith('```json'):
            analysis_json=analysis_json.replace('```json', '').replace('```', '').strip()

        analysis_data=json.loads(analysis_json)


        return analysis_data

    except Exception as e:
        print(f"An error occurred with the LLM: {e}")
        return None