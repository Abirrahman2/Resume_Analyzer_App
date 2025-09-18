import os


def extract_skills(text):

    found_skills = []

    skills_db_path = os.path.join(os.path.dirname(__file__), 'db', 'skills.txt')

    try:

        with open(skills_db_path, 'r', encoding='utf-8') as f:
            skills_db = [skill.strip().lower() for skill in f.read().split(',')]


        text = text.lower()
        for skill in skills_db:
            if skill in text:
                found_skills.append(skill)
    except FileNotFoundError:
        print(f"The skills file at {skills_db_path} was not found.")

    return found_skills