import fitz #pymupdf
import re

# Step-1: Getting a text from a sample resume which is in pdf format
def extract_txt_from_pdf(pdf_path):
    text=" "
    doc=fitz.open(pdf_path)
    for page in doc:
        text+=page.get_text()
    return text

# Testing
resume_txt=extract_txt_from_pdf("your_resume.pdf")
print(resume_txt)



# Step-2 Getting email address and phone number from resume
def extract_email_and_pno(text):
    # Regex for email
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

    # Regex for phone number
    phones = re.findall(r'(\+?\d{1,4}[\s-]?)?(\(?\d{3,5}\)?[\s-]?)?\d{5}[\s-]?\d{4}', text)

    #clear phnos
    phno_clear=[''.join(p) for p in phones]
    return emails,phno_clear

resume_text = """You can contact me at vishal.test@gmail.com or +91-98........"""
emails, phones = extract_email_and_pno(resume_text)

print("Emails:", emails)
print("Phone Numbers:", phones)



