if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Please log in first.")
    st.stop()
import streamlit as st
from helper import extract_text, clean_text, calculate_similarity

st.title("🏢 Recruiter Page")

st.subheader("📄 Upload Job Description")

jd_file = st.file_uploader("Upload Job Description", type=['pdf', 'docx', 'txt'])

if jd_file:
    jd_text = extract_text(jd_file)
    st.session_state["jd_text"] = jd_text  # 🔑 Store in session
    st.success("Job Description uploaded successfully!")
    st.text_area("📋 Job Description Preview", value=jd_text, height=250)

# 🧠 Perform Ranking
if "resume_text" in st.session_state and "jd_text" in st.session_state:
    if st.button("Rank Resume"):
        resume = clean_text(st.session_state["resume_text"])
        jd = clean_text(st.session_state["jd_text"])
        score = calculate_similarity(resume, jd)
        st.subheader("📊 Resume Ranking Result")
        st.write(f"**{st.session_state['resume_name']}** — Similarity Score: `{score:.2f}%`")
        st.success("Ranking Completed!")
else:
    st.info("Please make sure both Resume and Job Description are uploaded.")
