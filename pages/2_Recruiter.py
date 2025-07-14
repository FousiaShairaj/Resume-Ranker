import streamlit as st
from helper import extract_text, clean_text, calculate_similarity

# 🔐 Login check (only once)
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("🔒 Please log in first.")
    st.stop()

st.title("🏢 Recruiter Page")

# 📄 Upload JD
st.subheader("📄 Upload Job Description")
jd_file = st.file_uploader("Upload Job Description", type=['pdf', 'docx', 'txt'])

if jd_file:
    jd_text = extract_text(jd_file)
    st.session_state["jd_text"] = jd_text
    st.success("Job Description uploaded successfully!")
    st.text_area("📋 Job Description Preview", value=jd_text, height=250)

# 📊 Resume Ranking
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

# 💬 Feedback Section (place this after ranking logic)
st.subheader("💬 Give Feedback on Resume")

if "resume_text" in st.session_state and "resume_name" in st.session_state:
    selected_resume = st.session_state["resume_name"]
    feedback_input = st.text_area("Enter your feedback about the resume:")

    # Initialize feedback list
    if "feedback_list" not in st.session_state:
        st.session_state.feedback_list = []

    if st.button("Submit Feedback"):
        st.session_state.feedback_list.append({
            "resume": selected_resume,
            "feedback": feedback_input
        })
        st.success("✅ Feedback submitted.")

    # Display submitted feedback
    if st.session_state.feedback_list:
        st.subheader("📝 All Feedback")
        for item in st.session_state.feedback_list:
            st.markdown(f"**{item['resume']}** — {item['feedback']}")
    else:
        st.info("No feedback submitted yet.")
else:
    st.info("Upload and rank a resume first to give feedback.")
