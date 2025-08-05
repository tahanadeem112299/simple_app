import streamlit as st

st.title("🔐 Login System")

# Step 1: Set default state
if 'log_in' not in st.session_state:
    st.session_state['log_in'] = False

# Step 2: Show login form if not logged in
if not st.session_state['log_in']:
    username = st.text_input("Enter username: ")
    password = st.text_input("Enter password: ", type='password')
    login_button = st.button("Log in")
    
    if login_button:
        if username == 'admin' and password == '1234':
            st.session_state['log_in'] = True  # ✅ Corrected
            st.success("✅ Logged in successfully!")
        else:
            st.error("❌ Username or password is incorrect")

# Step 3: If logged in, show welcome message
if st.session_state['log_in']:  # ✅ Corrected
    st.success("👋 Welcome, admin!")
    if st.button("Log out"):
        st.session_state['log_in'] = False
