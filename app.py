from dotenv import load_dotenv
import os 
import streamlit as st
from process import extract_text ,create_chunks
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
load_dotenv()

# print(os.getenv('OPENAI_API_KEY'))

#set up streamlit page headings
st.set_page_config(page_title="PDF Analyzer")
st.header("Analyze your PDF")

# upload pdf
st.sidebar.header("PDF Analyzer")
pdf=st.sidebar.file_uploader("Upload your PDF",type="pdf")
if pdf is not None:
    #Extract the pdf text 
    text = extract_text(pdf)

    # split into chunks 
    chunks = create_chunks(text)

    #Create Embeddings and Knowledgebase
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks,embeddings)

    #Show user input
    question = st.text_input("ASK you questionabout your PDF")
    ask = st.button("Ask")

    if ask and question:
        docs = knowledge_base.similarity_search(question)
    
        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents = docs, question=question)
        st.write(response)