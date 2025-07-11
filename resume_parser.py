import pdfplumber
import os
from groq import Groq
import json

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_resume_info_from_groq(text):
    prompt = f"""
You are an intelligent resume parser. Extract the following details from the given resume text:

- Full Name
- Email
- Phone Number
- List of Key Skills
- Education (degree and institution, if present)
- Experience (company, role, and a brief summary)

Resume Text:
{text}

Return the extracted fields in JSON format with keys: name, email, phone, skills, education, experience.
Do NOT include any explanation or markdown like ```json or ``` in your response.
"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()

def extract_resume_info(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    structured_json = extract_resume_info_from_groq(text)
    try:
        return json.loads(structured_json)
    except json.JSONDecodeError:
        print("Error parsing JSON from Groq response.")
        return {}