import streamlit as st
from helper import extract_text

st.title("🏢 Recruiter Page")

st.subheader("📄 Upload Job Description")

jd_file = st.file_uploader("Upload Job Description", type=['pdf', 'docx', 'txt'])

if jd_file:
    jd_text = extract_text(jd_file)
    st.success("Job Description uploaded successfully!")
    st.text_area("📋 Job Description Preview", value=jd_text, height=250)
