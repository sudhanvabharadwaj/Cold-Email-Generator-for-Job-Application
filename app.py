import streamlit as st
from scraper import extract_job_details
from resume_parser import extract_resume_info
from prompt_builder import build_prompt
from llm_runner import generate_email

st.title("Cold Email Generator for Job Applications")

job_url = st.text_input("Job Posting URL")
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Generate Cold Email"):
    if not job_url or not resume_file:
        st.warning("Please provide both the job URL and your resume.")
    else:
        with st.spinner("Extracting job details..."):
            job_desc = extract_job_details(job_url)
        with st.spinner("Parsing resume..."):
            # Save uploaded file temporarily
            temp_path = r"resumes\temp_resume.pdf"
            with open(temp_path, "wb") as f:
                f.write(resume_file.read())
            resume_data = extract_resume_info(temp_path)
        with st.spinner("Building prompt and generating email..."):
            prompt = build_prompt(job_desc, resume_data)
            email = generate_email(prompt)
        st.success("Cold Email Generated!")
        st.text_area("Generated Email", email, height=300)