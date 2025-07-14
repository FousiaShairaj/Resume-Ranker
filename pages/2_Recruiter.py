# 📊 Resume Ranking
if "resume_text" in st.session_state and "jd_text" in st.session_state:
    if st.button("Rank Resume"):
        resume = clean_text(st.session_state["resume_text"])
        jd = clean_text(st.session_state["jd_text"])
        score = calculate_similarity(resume, jd)
        st.session_state["score"] = score
        st.session_state["show_feedback"] = True  # ✅ Set flag
        st.success("Ranking Completed!")

# Show the score if available
if "score" in st.session_state:
    st.subheader("📊 Resume Ranking Result")
    st.write(f"**{st.session_state['resume_name']}** — Similarity Score: `{st.session_state['score']:.2f}%`")

# 💬 Feedback Section: only visible after ranking
if st.session_state.get("show_feedback", False):
    st.subheader("💬 Give Feedback on Resume")

    selected_resume = st.session_state["resume_name"]
    feedback_input = st.text_area("Enter your feedback:", key="feedback_input")

    # Initialize feedback list
    if "feedback_list" not in st.session_state:
        st.session_state.feedback_list = []

    if st.button("Submit Feedback"):
        if feedback_input.strip() != "":
            st.session_state.feedback_list.append({
                "resume": selected_resume,
                "feedback": feedback_input.strip()
            })
            st.success("✅ Feedback submitted.")
            # Clear input after submission
            st.session_state.feedback_input = ""
        else:
            st.warning("⚠️ Please enter feedback before submitting.")

    # Display all submitted feedback
    if st.session_state.feedback_list:
        st.subheader("📝 All Feedback")
        for item in st.session_state.feedback_list:
            st.markdown(f"**{item['resume']}** — {item['feedback']}")
