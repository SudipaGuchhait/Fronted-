import streamlit as st

# Page config
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# Session state for page tracking
if "page" not in st.session_state:
    st.session_state.page = "login"

# Background & CSS
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(to top, rgba(0,0,0,0.5)50%,rgba(0,0,0,0.5)50%),url("https://images.unsplash.com/photo-1702365202240-ecf532732c76?q=80&w=1932&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Title */
.login-box h2 {
    color: white;
    margin-bottom: 1.5rem;
    front-size: 1.5rem;
}

/* Inputs */
input {
    border-radius: 8px !important;
    padding: 5px !important;
    font-size: 0.9rem !important;
    height: 35px !important;
}

/* Buttons */
.stButton>button {
    background-color: #3a4ef0;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.4rem 0.5rem;
    font-size: 0.9rem;
    font-weight: bold;
    cursor: pointer;
    width: 120%;
    margin-top: 1rem;
}
.stButton>button:hover {
    background-color: #2d3ecf;
}

/* Links */
a {
    color: #4da6ff;
    text-decoration: none;
    font-size: 0.85rem;
}
a:hover {
    text-decoration: underline;
}

/* Remember & Forgot */
.remember-forgot {
    display: flex;
    justify-content: space-between;
    font-size: 0.8rem;
    color: white;
    margin-top: 0.3rem;
}
</style>
""", unsafe_allow_html=True)


# LOGIN PAGE
def login_page():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("<h2>Login</h2>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Remember / Forgot row
    c1, c2 = st.columns([1, 1])
    with c1:
        remember = st.checkbox("Remember me")
    with c2:
        st.markdown('<div style="text-align:right;"><a href="#">Forgot password?</a></div>', unsafe_allow_html=True)

    # ---- Centered LOGIN button ----
    left, center, right = st.columns([1, 2, 1])   # define columns here
    with center:
        login_clicked = st.button("Login", use_container_width=True)

    if login_clicked:
        if username == "admin" and password == "1234":
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

    # ---- Centered "Sign up" button (navigates to register page) ----
    #st.markdown("<br>", unsafe_allow_html=True)
    l2, mid, r2 = st.columns([1, 2, 1])
    with mid:
        if st.button("Sign up", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# REGISTRATION PAGE
def registration_page():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("<h2>Register</h2>", unsafe_allow_html=True)

    new_user = st.text_input("Create Username")
    new_pass = st.text_input("Create Password", type="password")
    confirm_pass = st.text_input("Confirm Password", type="password")
    email = st.text_input("Email")

    # ---- Centered Register button ----
    left, center, right = st.columns([1, 2, 1])
    with center:
        if st.button("Register", use_container_width=True):
            if new_pass != confirm_pass:
                st.error("Passwords do not match")
            else:
                st.success(f"Account created for {new_user}!")
                st.session_state.page = "login"
                st.rerun()

    # ---- Centered Back to Login button ----
    l2, mid, r2 = st.columns([1, 2, 1])
    with mid:
        if st.button("Back to Login", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# PAGE ROUTER
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "register":
    registration_page()


