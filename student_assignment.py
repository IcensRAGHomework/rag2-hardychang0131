from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    return load_pdf(q1_pdf)[-1]

def hw02_2(q2_pdf):
    docs = load_pdf(q2_pdf)
    text = ""
    for doc in docs:
        text += doc.page_content + "\n"
    
    spliter = RecursiveCharacterTextSplitter(separators=["第 [一二三四五六七八九十百千零]+ 章","第 \\d+-?\\d* 條\n"],
                                             chunk_size = 0,
                                             chunk_overlap = 0,
                                             is_separator_regex=True,
                                             keep_separator= True)
    return len(spliter.create_documents([text]))


def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs
