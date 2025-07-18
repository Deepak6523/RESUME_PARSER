import re
import fitz  
import spacy


nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ''
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return ''

def extract_name(doc):
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return ""

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else ""

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3}[-.\s]?)?(\d{10}|\d{3}[-.\s]?\d{3}[-.\s]?\d{4})', text)
    return match.group(0) if match else ""

def extract_links(text):
    links = re.findall(r'(https?://[^\s]+)', text)
    linkedin = next((l for l in links if "linkedin.com" in l), "")
    github = next((l for l in links if "github.com" in l), "")
    return linkedin, github

def extract_summary(text):
    match = re.search(r'(Objective|Summary|Professional Summary)\s*[:\-]*\s*(.*?)\n[A-Z]', text, re.DOTALL | re.IGNORECASE)
    return match.group(2).strip() if match else ""

def extract_skills(text):
    
    skill_keywords = [
        "python", "java", "c++", "sql", "excel", "machine learning", "deep learning",
        "flask", "django", "react", "node.js", "docker", "git", "aws", "nlp"
    ]
    text = text.lower()
    found_skills = [skill for skill in skill_keywords if skill in text]
    return list(set(found_skills))

def extract_education(text):
    education_keywords = ['bachelor', 'master', 'b.tech', 'm.tech', 'b.sc', 'm.sc', 'mba', 'phd', 'university', 'college', 'school']
    lines = text.lower().split('\n')
    return list(set([line for line in lines if any(word in line for word in education_keywords)]))

def extract_experience(text):
    pattern = re.compile(r'(Experience|Work Experience|Professional Experience)\s*[:\-]*\s*(.*?)\n\n', re.DOTALL | re.IGNORECASE)
    match = pattern.search(text)
    if match:
        return match.group(2).strip().split('\n')
    return []

def extract_projects(text):
    lines = text.split('\n')
    project_titles = []
    collecting = False
    for line in lines:
        if re.search(r'project', line, re.IGNORECASE):
            collecting = True
            continue
        if collecting:
            if line.strip() == '' or re.match(r'[A-Z ]{4,}', line):  
                break
            if len(line.strip()) > 4:
                project_titles.append(line.strip())
    return list(set(project_titles))

def extract_certifications(text):
    cert_keywords = ['certification', 'certified', 'certificate', 'credential']
    lines = text.lower().split('\n')
    return list(set([line.strip() for line in lines if any(word in line for word in cert_keywords)]))

def extract_languages(text):
    known_languages = ['english', 'hindi', 'french', 'german', 'spanish', 'tamil', 'telugu', 'kannada', 'bengali']
    text_lower = text.lower()
    return list(set([lang for lang in known_languages if lang in text_lower]))

def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    if not text:
        print("❌ Failed to extract text from the resume.")
        return

    doc = nlp(text)

    data = {
        "Name": extract_name(doc),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "LinkedIn": extract_links(text)[0],
        "GitHub": extract_links(text)[1],
        "Summary": extract_summary(text),
        "Skills": extract_skills(text),
        "Education": extract_education(text),
        "Experience": extract_experience(text),
        "Projects": extract_projects(text),
        "Certifications": extract_certifications(text),
        "Languages Known": extract_languages(text),
    }

    print("\n✅ Extracted Resume Data:\n")
    for key, value in data.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"  - {item}")
        else:
            print(f"{key}: {value}")


if __name__ == "__main__":
    file_path = input("📎 Enter the path to the resume PDF: ")
    parse_resume(file_path)
