from urllib3.filepost import writer

from analyzer import parse_job_description,calculate_match_score
from parser import extract_text_from_pdf, extract_text_from_docx
from extractor import extract_contact_info
from skills import  extract_skills
import  csv
import os
import pandas as pd

RESUMES_FOLDER=r"D:\RESUME_DIR"
JD_FILE_PATH=os.path.join("Job_Description","job_description.txt")

def main():


    jd_info=parse_job_description(JD_FILE_PATH)
    if not jd_info["required_skills"]:
       print("unable to extract required skills")
       return
    print(f"Required Skills are: {jd_info["required_skills"]}")

    if not os.path.exists(RESUMES_FOLDER):
        os.makedirs(RESUMES_FOLDER)
        print(f"Created a new folder: '{RESUMES_FOLDER}'. Please place your resumes here.")
        return

    files = os.listdir(RESUMES_FOLDER)
    if not files:
        print(f"files not found in the '{RESUMES_FOLDER}' folder. Please upload resumes.")
        return
    all_candidate_result=[]
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
            calculate_score,matched_skills,missing_skills=calculate_match_score(found_skills,jd_info)
            candidate_data={
                'filename':filename,
                'email':contact_info['email'],
                'phone':contact_info['phone'],
                'skills_found':','.join(found_skills),
                'missing_skill':missing_skills,
                'match_score':calculate_score
            }
            all_candidate_result.append(candidate_data)
            print(f"Email:{contact_info['email']}")
            print(f"Phone:{contact_info['phone']}")
            print(f"Skills Found: {', '.join(found_skills)}")
            print(f"Obtained score:{calculate_score:.3f}")
        else:
            print("Failed to extract data from participant")
    if all_candidate_result:

        df=pd.DataFrame(all_candidate_result)
        df=df.sort_values(by='match_score',ascending=False)
        df.to_csv('analysis_results_by_skills.csv',index=False)
    else:
        print("we have no candidates")
        #fieldnames = ['filename', 'email', 'phone', 'skills_found','missing_skill', 'match_score']
        #filename = "all_analysis_results.csv"

    """with open(filename,'w',newline='',encoding='utf-8') as csvfile:

            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_candidate_result)"""



if __name__ == "__main__":
    main()