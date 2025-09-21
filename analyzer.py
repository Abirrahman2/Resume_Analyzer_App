import os
import re


def parse_job_description(jd_path):

    jd_info = {
        'required_skills': [],
        'required_experience': 0
    }

    try:
        with open(jd_path, 'r', encoding='utf-8') as f:
            jd_text = f.read().lower()

            skills_section_match = re.search(r'required skills:(.*?)(required experience|education|responsibilities|$)',
                                             jd_text, re.DOTALL)
            if skills_section_match:
                skills_text = skills_section_match.group(1).strip()

                skills_list = re.split(r'[\n,]', skills_text)
                cleaned_skills = [re.sub(r'[\s-]+', ' ', skill).strip() for skill in skills_list if skill.strip()]
                jd_info['required_skills'] = cleaned_skills

            experience_match = re.search(r'(\d+)\+\s*years', jd_text)
            if experience_match:
                jd_info['required_experience'] = int(experience_match.group(1))

    except FileNotFoundError:
        print(f"Error: Job description file at {jd_path} not found.")

    return jd_info


def calculate_match_score(candidate_skills, jd_info):

    required_skills = set(jd_info['required_skills'])
    candidate_skills_set = set(candidate_skills)

    if not required_skills:
        return 0.0, [], []

    matched_skills = candidate_skills_set.intersection(required_skills)

    missing_skills = required_skills.difference(matched_skills)

    score = (len(matched_skills) / len(required_skills)) * 100

    return round(score, 2), list(matched_skills), list(missing_skills)