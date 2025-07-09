import requests
from bs4 import BeautifulSoup
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key="GROQ_API_KEY")

def fetch_job_posting_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        text_content = soup.get_text(separator="\n")
        return text_content
    except requests.RequestException as e:
        print(f"Error fetching job posting: {e}")
        return None
    
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
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()