import streamlit as st
# Page config
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# Background Image (CSS trick)
st.markdown("""
<style>
/* Background Image */
[data-testid="stAppViewContainer"]{
    background-image:linear-gradient(to top, rgba(0,0,0,0.5)50%,rgba(0,0,0,0.5)50%), url("https://images.unsplash.com/photo-1702365202240-ecf532732c76?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.Login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.login h1{
    text-align: center;
    color: white;
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.1);
}

.login-box h2 {
    color: white;
}

.login-box label {
    color: white;
    text-align: left;
    display: block;
    margin-top: 10px;
}

.stButton>button {
    background-color: #f5b041;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    font-weight: bold;
    cursor: pointer;
    justify-content: center;
    margin-top: 2rem;
    text-align: center;`
}

.stButton>button:hover {
    background-color: #e6a732;
}

a {
    color: yellow;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
""" , unsafe_allow_html=True)

#st.markdown(page_bg_img, unsafe_allow_html=True)

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
    
    st.markdown('</div>', unsafe_allow_html=True)

# Logic for button
if login_btn:
    if username == "admin" and password == "1234":
        st.success("Login successful!")
    else:
        st.error("Invalid username or password")
#
