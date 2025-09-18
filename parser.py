import fitz

def extract_text_from_pdf(pdf_path):
    text=""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text+=page.get_text()
    except Exception as e:
        print(f"error occurs{pdf_path}:{e}")
    return  text