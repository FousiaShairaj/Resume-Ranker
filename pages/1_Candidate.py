if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Please log in first.")
    st.stop()
import streamlit as st
from helper import extract_text

st.title("🧑‍💼 Candidate Page")

st.write("Upload your resume below.")

resume_file = st.file_uploader("Upload Resume (PDF, DOCX, TXT)", type=['pdf', 'docx', 'txt'])

if resume_file:
    resume_text = extract_text(resume_file)
    st.success("Resume uploaded successfully!")
    st.session_state["resume_text"] = resume_text  # 🔑 Store in session
    st.session_state["resume_name"] = resume_file.name
    st.text_area("Resume Preview", value=resume_text, height=200)
