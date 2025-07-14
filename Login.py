import streamlit as st

# Simulated in-memory user database
if "users" not in st.session_state:
    st.session_state.users = {}  # Format: username: {"password": ..., "role": ...}

# Initialize session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""

# Heading and layout
st.set_page_config(page_title="AI Resume Ranker", layout="centered")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1024px-React-icon.svg.png", width=100)
st.markdown("<h1 style='text-align: center;'>AI RESUME RANKER</h1>", unsafe_allow_html=True)

# Choose between Login and Sign Up
mode = st.radio("Choose an option:", ["Login", "Sign Up"])

if mode == "Sign Up":
    st.subheader("🔑 Sign Up")
    new_username = st.text_input("Create Username")
    new_password = st.text_input("Create Password", type="password")
    new_role = st.selectbox("Select Role", ["candidate", "recruiter"])
    if st.button("Register"):
        if new_username in st.session_state.users:
            st.error("Username already exists. Try another.")
        else:
            st.session_state.users[new_username] = {
                "password": new_password,
                "role": new_role
            }
            st.success("User registered successfully. Please log in.")

elif mode == "Login":
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    selected_role = st.selectbox("Log in as", ["candidate", "recruiter"])

    if st.button("Login"):
        user = st.session_state.users.get(username)
        if user and user["password"] == password and user["role"] == selected_role:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = selected_role
            st.success(f"✅ Logged in as {selected_role}")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username, password, or role.")

# After login
if st.session_state.logged_in:
    st.success(f"Welcome, {st.session_state.username} ({st.session_state.role})")
    
    if st.session_state.role == "candidate":
        st.page_link("pages/1_Candidate.py", label="Go to Candidate Page")
    elif st.session_state.role == "recruiter":
        st.page_link("pages/2_Recruiter.py", label="Go to Recruiter Page")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.experimental_rerun()
