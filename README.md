# AI-Powered Resume Analyzer (Flask Web App)
##  Project Overview
This application is a full-stack web tool designed to streamline the recruitment process by efficiently analyzing candidate resumes against a job description. It utilizes a dual-analysis approach: a traditional keyword parser for speed and a powerful Large Language Model (LLM) for contextual evaluation.
##  Key Features
* **Dual-Analysis:** Provides both a fast, traditional keyword-based match score and an in-depth, AI-driven analysis (strengths, weaknesses, summary).
* **Gemini API Integration:** Leverages the **Gemini 2.5 Flash** model for contextual understanding and structured JSON output.
* **Multi-Format Support:** Processes resumes in common formats (`.pdf`, `.docx`) and job descriptions from `.txt` files.
* **Full-Stack Implementation:** Built using **Python (Flask)** for the backend and a responsive front-end for easy file uploading and clear result visualization.

##  Stack
* **Backend Framework:** Flask
* **Artificial Intelligence:** Google Gemini API
* **File Parsing:** `fitz` (PyMuPDF) for PDF, `python-docx` for DOCX
* **Data Handling:** `pandas`, `os`, `dotenv`
* **Frontend:** HTML5 and CSS

## Screenshots
<img width="978" height="293" alt="resumeapp1" src="https://github.com/user-attachments/assets/d0ecbfd0-b79d-4ca7-bf39-b141dd5841e4" />
<img width="953" height="220" alt="resumeapp2" src="https://github.com/user-attachments/assets/57bcec67-62fb-4c8f-b6ea-7750355fb5f7" />
<img width="926" height="529" alt="resumeapp3" src="https://github.com/user-attachments/assets/6dac2bd5-7ead-4b95-9709-2152e03ca758" />

## Batch Analysis
