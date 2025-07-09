from resume_parser import extract_resume_info
from prompt_builder import build_prompt
from llm_runner import generate_email
from scraper import extract_job_details

def main():
    job_url = input("Enter the job posting URL:").strip()
    resume_path = input("Enter path to resume (PDF): ").strip()

    print("🔍 Extracting job info...")
    job_description_raw = extract_job_details(job_url)

    print("📄 Parsing resume...")
    resume_data = extract_resume_info(resume_path)

    print("🧠 Building LLM prompt...")
    prompt = build_prompt(job_description_raw, resume_data)

    print("✉️ Generating cold email...")
    email = generate_email(prompt)

    print("\n✅ Cold Email Generated:\n")
    print(email)

    with open("emails/generated_email.txt", "w") as f:
        f.write(email)

if __name__ == "__main__":
    main()