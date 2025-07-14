import streamlit as st

# Dummy user store for demo
users = {
    "candidate@example.com": {"password": "pass123", "role": "candidate"},
    "recruiter@example.com": {"password": "pass456", "role": "recruiter"}
}

st.set_page_config(page_title="Login | AI Resume Ranker")

st.title("🔐 Login to AI Resume Ranker")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

if not st.session_state.logged_in:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns([1, 3])
    with col1:
        login_btn = st.button("Login")
    with col2:
        signup_btn = st.button("Sign up (Not implemented)")

    if login_btn:
        user = users.get(email)
        if user and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = user["role"]
            st.success(f"Logged in as {st.session_state.role.capitalize()} ✅")
            st.experimental_rerun()
        else:
            st.error("Invalid email or password")

else:
    st.success(f"✅ You are logged in as a **{st.session_state.role}**")
    if st.session_state.role == "candidate":
        st.page_link("pages/1_Candidate.py", label="Go to Candidate Page")
    elif st.session_state.role == "recruiter":
        st.page_link("pages/2_Recruiter.py", label="Go to Recruiter Page")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.experimental_rerun()
