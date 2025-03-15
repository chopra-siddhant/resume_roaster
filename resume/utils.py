import os
from PyPDF2 import PdfReader
import docx

def parse_resume(file_obj):
    """
    Parse the uploaded resume file (PDF or DOCX) and extract text.
    """
    filename = file_obj.name
    ext = os.path.splitext(filename)[1].lower()

    if ext == '.pdf':
        reader = PdfReader(file_obj)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    elif ext in ['.doc', '.docx']:
        # For DOCX files; note: for .doc files you might need another library.
        document = docx.Document(file_obj)
        text = "\n".join([para.text for para in document.paragraphs])
        return text
    else:
        # Fallback: assume it's a plain text file.
        return file_obj.read().decode('utf-8')
