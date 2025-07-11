# Cold-Email-Generator-for-Job-Application

A streamlined tool that generates personalized, warm cold emails to recruiters based on a job posting and your resume. Powered by LLMs, this app extracts job details and resume information, then crafts a tailored email ready to send.

---
## Features

- **Job Scraping:** Extracts and summarizes job title, company, responsibilities, requirements, and location from any job posting URL.
- **Resume Parsing:** Extracts your name, email, skills, education, and experience from your uploaded PDF resume.
- **Personalized Email Generation:** Uses a Jinja2 prompt template and LLM to generate a confident, human, and fact-based cold email.
- **Streamlit Frontend:** Simple web UI for uploading your resume and entering a job URL.
- **LLM Integration:** Uses Groq API with Llama 3 for all extraction and generation tasks.

---
## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cold-email-generator-for-job-application.git
cd cold-email-generator-for-job-application
```

### 2. Install Dependencies

It's recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a .env file in the project root with your Groq API key:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Download ChromeDriver

This app uses Selenium for scraping.

- Download ChromeDriver matching your Chrome version.
- Place the ```chromedriver.exe``` in your PATH or project root.

### 5. Run the App

```bash
streamlit run app.py
```

---
## Usage

#### 1. Enter the job posting URL (e.g., from LinkedIn, Indeed, etc.).
#### 2. Upload your resume as a PDF file.
#### 3. Click "Generate Cold Email".
#### 4. Copy the generated email and send it to the recruiter!

---
## Customization

- **Prompt Template:** Edit ```templates/prompt_template.txt``` to change the email style or structure.
- **LLM Model:** Change the model name in ```llm_runner.py``` and ```scraper.py``` if you want to use a different LLM variant.

---