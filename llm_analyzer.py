import openai
import os


def analyze_with_llm(resume_text, jd_text):

    openai.api_key = os.getenv("OPENAI_API_KEY")
    # Or, for quick testing: openai.api_key = "YOUR_API_KEY"

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
        response = openai.chat.completions.create(
            model="gpt-4",  # Or another suitable model like gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract the JSON string from the response
        analysis_json = response.choices[0].message.content.strip()

        # Clean up any extra text that the LLM might include
        if analysis_json.startswith("```json"):
            analysis_json = analysis_json[7:-3].strip()

        return json.loads(analysis_json)

    except Exception as e:
        print(f"An error occurred with the LLM API call: {e}")
        return None