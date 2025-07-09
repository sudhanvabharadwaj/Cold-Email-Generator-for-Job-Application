from jinja2 import Template

def build_prompt(job, resume):
    with open("templates/prompt_template.txt", "r") as f:
        template = Template(f.read())
    return template.render(job=job, resume=resume)