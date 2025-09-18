
from parser import extract_text_from_pdf, extract_text_from_docx
from extractor import extract_contact_info
from skills import  extract_skills
import os

RESUMES_FOLDER=r"D:\RESUME_DIR"


def main():

    if not os.path.exists(RESUMES_FOLDER):
        os.makedirs(RESUMES_FOLDER)
        print(f"Created a new folder: '{RESUMES_FOLDER}'. Please place your resumes here.")
        return


    files = os.listdir(RESUMES_FOLDER)

    if not files:
        print(f"files not found in the '{RESUMES_FOLDER}' folder. Please upload resumes.")
        return

    for filename in files:
        file_path = os.path.join(RESUMES_FOLDER, filename)
        extracted_text=""
        print(f"\n{filename}")
        if filename.lower().endswith(".pdf"):
            extracted_text = extract_text_from_pdf(file_path)
            if extracted_text:
                print("extracted successfully")
            else:
                print("Failed to extract text.")

        elif filename.lower().endswith(".docx"):

             extracted_text = extract_text_from_docx(file_path)
             if extracted_text:
                 print("extracted successfully")

        else:
            print(f"unsupported file type: '{filename}'")

        if extracted_text:
            contact_info=extract_contact_info(extracted_text)
            found_skills=extract_skills(extracted_text)
            print(f"Email:{contact_info['email']}")
            print(f"Phone:{contact_info['phone']}")
            print(f"Skills Found: {', '.join(found_skills)}")


if __name__ == "__main__":
    main()