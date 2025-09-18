from logging import exception

from docx import Document

import fitz
from pygments.formatters.terminal256 import EscapeSequence


def extract_text_from_pdf(pdf_path):
    text=""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text+=page.get_text()
    except Exception as e:
        print(f"error occurs{pdf_path}:{e}")
    return  text
def extract_text_from_docx(docx_path):
    text=""
    try:
        doc=Document(docx_path)
        for p in doc.paragraphs:
            text+=p.text+"\n"
    except Exception as e:
        print(f"error occurs:{e}")
    return text
