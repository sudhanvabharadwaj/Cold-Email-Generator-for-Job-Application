import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "main.py",
    "app.py",
    "scraper.py",
    "resume_parser.py",
    "prompt_builder.py",
    "llm_runner.py",
    "templates/prompt_template.txt",
    "resumes/sample_resume.pdf",
    "emails/generated_email.txt",
    "requirements.txt",
    "README.md",
    ".env"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            if filename.endswith(".pdf"):
                f.write("%PDF-1.4\n%EOF")  # dummy content for a valid header
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")