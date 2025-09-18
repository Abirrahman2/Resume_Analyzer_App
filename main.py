from parser import extract_text_from_pdf
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

        print(f"\n{filename}")
        if filename.lower().endswith(".pdf"):
            extracted_text = extract_text_from_pdf(file_path)
            if extracted_text:
                print("extracted successfully")
            else:
                print("Failed to extract text.")

        elif filename.lower().endswith(".docx"):

            print("DOCX file.")
            # extracted_text = extract_text_from_docx(file_path) # Future code

        else:
            print(f"Skipping unsupported file type: '{filename}'")



if __name__ == "__main__":
    main()