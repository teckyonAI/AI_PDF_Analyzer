from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def extract_text(pdf):
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
        return text
    else:
        pdf = None

def create_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=500,
        chunk_overlap=200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks

    

