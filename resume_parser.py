import os
import docx2txt
from pyresparser import ResumeParser

def extract_resume_info(file_path):
    data = ResumeParser(file_path).get_extracted_data()
    return {
        "name": data.get("name", "N/A"),
        "email": data.get("email", "N/A"),
        "skills": data.get("skills", []),
        "education": data.get("education", []),
        "experience": data.get("experience", []),
        "summary": data.get("summary", "N/A")
    }