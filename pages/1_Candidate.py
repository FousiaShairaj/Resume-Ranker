import streamlit as st
from helper import extract_text

st.title("🧑‍💼 Candidate Page")

st.write("Upload your resume below.")

resume_file = st.file_uploader("Upload Resume (PDF, DOCX, TXT)", type=['pdf', 'docx', 'txt'])

if resume_file:
    text = extract_text(resume_file)
    st.success("Resume uploaded successfully!")
    st.text_area("Resume Preview (Extracted Text)", value=text, height=200)
