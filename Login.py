import streamlit as st

# Initialize user store in session (for demo only)
if "users" not in st.session_state:
    st.session_state.users = {}  # username: {password, role}

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = ""

# Choose mode: Login or Signup
mode = st.radio("Choose an option:", ["Login", "Sign Up"])

if mode == "Sign Up":
    st.title("📝 Sign Up")
    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")
    role = st.selectbox("I am a...", ["candidate", "recruiter"])
    
    if st.button("Sign Up"):
        if username in st.session_state.users:
            st.error("❌ Username already exists. Try another.")
        else:
            st.session_state.users[username] = {
                "password": password,
                "role": role
            }
            st.success("✅ Signup successful! Please log in.")

elif mode == "Login":
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        user = st.session_state.users.get(username)
        if user and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.role = user["role"]
            st.session_state.username = username
            st.success(f"✅ Logged in as {st.session_state.role}")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid credentials.")

# After login
if st.session_state.logged_in:
    st.success(f"Welcome, **{st.session_state.username}** ({st.session_state.role})")
    
    if st.session_state.role == "candidate":
        st.page_link("pages/1_Candidate.py", label="Go to Candidate Page")
    elif st.session_state.role == "recruiter":
        st.page_link("pages/2_Recruiter.py", label="Go to Recruiter Page")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.username = ""
        st.experimental_rerun()
