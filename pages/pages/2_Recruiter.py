import streamlit as st
from helper import extract_text, clean_text, calculate_similarity

st.title("🏢 Recruiter Page")

resumes = {}
job_description_text = ""
feedback_data = []

jd_file = st.file_uploader("Upload Job Description", type=['pdf', 'docx', 'txt'])
if jd_file:
    job_description_text = extract_text(jd_file)
    st.success("Job Description uploaded!")

uploaded_files = st.file_uploader("Upload Resumes", type=['pdf', 'docx', 'txt'], accept_multiple_files=True)
for file in uploaded_files:
    resumes[file.name] = extract_text(file)

if st.button("Rank Resumes"):
    if not job_description_text or not resumes:
        st.warning("Please upload both Job Description and Resumes.")
    else:
        st.subheader("📊 Resume Ranking Results")
        cleaned_jd = clean_text(job_description_text)
        results = []
        for name, text in resumes.items():
            cleaned_resume = clean_text(text)
            score = calculate_similarity(cleaned_resume, cleaned_jd)
            results.append((name, score))
        ranked = sorted(results, key=lambda x: x[1], reverse=True)
        for name, score in ranked:
            st.write(f"**{name}** — Similarity Score: `{score:.2f}%`")
        st.success("Ranking Completed!")
