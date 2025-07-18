# 🧠 AI Resume Parser

A powerful AI-based Resume Parser built with Python that extracts structured data from PDF or DOCX resumes — helping automate the screening process for HR and recruitment systems.

---

## 📌 Features

- 🔍 Extracts Name, Email, Phone, LinkedIn, GitHub
- 🧠 Uses NLP to identify Skills, Education, Certifications, Projects, Experience
- 📄 Supports both `.pdf` and `.docx` formats
- 🧾 Exports extracted information into a clean **PDF summary**
- ⚙️ Simple CLI for local use

---

## 🛠️ Tech Stack

- **Python 3.12**
- [spaCy](https://spacy.io/) – NLP for text segmentation  
- [nltk](https://www.nltk.org/) – Stopword filtering  
- [textract](https://textract.readthedocs.io/en/stable/) – Universal document text extraction  
- [fpdf](https://pyfpdf.readthedocs.io/en/latest/) – PDF export  
- **Regex** – Pattern matching for emails, phones, links  
- **Command-line Interface**

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/yourusername/ai-resume-parser.git
cd ai-resume-parser
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


📚 Required NLTK & spaCy Models
# Inside a Python shell or script
import nltk
nltk.download('stopwords')

# In terminal
python -m spacy download en_core_web_sm

🖥️ Usage
python resume_parser.py

When prompted, provide the full path to the resume file (PDF or DOCX).
The script will:
Parse the resume
Display the extracted info in the terminal
Generate a PDF summary as parsed_resume_output.pdf

📂 Project Structure
resume_parser/
│
├── resume_parser.py         # Main script
├── requirements.txt         # All dependencies
├── sample_resume.pdf        # Test file
├── parsed_resume_output.pdf # Output generated
└── README.md

✅ Extracted Resume Data:

Name: Anuj Singh Solanki
Email: anujsolanki422@gmail.com
Phone: +91 7877890595
LinkedIn: https://linkedin.com/in/deepak-
GitHub: https://github.com/Deepak6523
Skills: java, git, sql, react
Education: B.Tech in AI & Data Science, Coding Club Member, etc.
Certifications: AI Certificate - HP
Languages Known: English, Hindi
Projects: AI Resume Parser, etc.


👥 Credits
Built with ❤️ by Deepak Singh Chouhan
Developed as part of my learning with Pinnacle Lab



