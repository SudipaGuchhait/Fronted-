import streamlit as st
import base64

# Function to set background imag


# Page config
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# Background Image (CSS trick)
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-color: yellow;
    background-image: url("https://images.unsplash.com/photo-1506744038136-
    background-size: cover;
    background-position: center;
}}
.Login-page {{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}}
.login-box {{
    background-color: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 10px;
    text-align: center;
    width: 350px;
    margin: auto;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    color: white;
    font-family: 'Arial', sans-serif;
}}

.login-box h2 {{
    color: white;
}}

.login-box label {{
    color: white;
    text-align: left;
    display: block;
    margin-top: 10px;
}}

.stButton>button {{
    background-color: #f5b041;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    font-weight: bold;
    cursor: pointer;
}}

.stButton>button:hover {{
    background-color: #e6a732;
}}

a {{
    color: yellow;
    text-decoration: none;
}}
a:hover {{
    text-decoration: underline;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Login Form UI
with st.container():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("<h2>Login</h2>", unsafe_allow_html=True)
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    remember = st.checkbox("Remember Me")
    st.markdown('<a href="#">Forgot Password?</a>', unsafe_allow_html=True)
    login_btn = st.button("Login")
    st.markdown("Don't have an account? <a href='#'>Sign Up_btn</a>", unsafe_allow_html=True)
    st.write("Or login with:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[🐦](#)")
    with col2:
        st.markdown("[📘](#)")
    with col3:
        st.markdown("[💼](#)")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Logic for button
if login_btn:
    if username == "admin" and password == "1234":
        st.success("Login successful!")
    else:
        st.error("Invalid username or password")