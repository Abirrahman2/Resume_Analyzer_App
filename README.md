# AI-Powered Resume Analyzer (Flask Web App)
##  Project Overview
This application is a full-stack web tool designed to streamline the recruitment process by efficiently analyzing candidate resumes against a job description. It utilizes a dual-analysis approach: a traditional keyword parser for speed and a powerful Large Language Model (LLM) for contextual evaluation.
##  Key Features
* **Dual-Analysis:** Provides both a fast, traditional keyword-based match score and an in-depth, AI-driven analysis (strengths, weaknesses, summary).
* **Gemini API Integration:** Leverages the **Gemini 2.5 Flash** model for superior contextual understanding and structured JSON output.
* **Multi-Format Support:** Processes resumes in common formats (`.pdf`, `.docx`) and job descriptions from `.txt` files.
* **Full-Stack Implementation:** Built using **Python (Flask)** for the backend and a responsive front-end (HTML/CSS) for easy file uploading and clear result visualization.

##  Stack
* **Backend Framework:** Flask
* **Artificial Intelligence:** Google Gemini API (`google-generativeai`)
* **File Parsing:** `fitz` (PyMuPDF) for PDF, `python-docx` for DOCX
* **Data Handling:** `pandas`, `os`, `dotenv`
* **Frontend:** HTML5 and CSS

## Screenshots
![resumeapp1.png](images%2Fresumeapp1.png)