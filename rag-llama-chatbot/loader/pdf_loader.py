from pypdf import PdfReader

def load_pdf(file_obj):
    reader = PdfReader(file_obj)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
