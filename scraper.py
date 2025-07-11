import os
import requests
from bs4 import BeautifulSoup
from groq import Groq
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def fetch_job_posting_html(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        text_content = soup.get_text(separator="\n")
        return text_content
    finally:
        driver.quit()
    
def extract_job_details(url):
    raw_text = fetch_job_posting_html(url)
    prompt = f"""
Given the raw text content of a job posting webpage, extract and summarize the following in plain text:
- Job Title
- Company Name
- Key Responsibilities (bullet points)
- Requirements or Qualifications (bullet points)
- Location (if mentioned)

Here is the content:
{raw_text}
"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()