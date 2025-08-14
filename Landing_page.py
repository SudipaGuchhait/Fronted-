import streamlit as st

# --- Page config ---
st.set_page_config(page_title="Trip", layout="wide")

# --- Custom CSS ---

st.markdown("""
<style>
/* Background Image */
[data-testid="stAppViewContainer"] {
    background-image:linear-gradient(to top, rgba(0,0,0,0.5)50%,rgba(0,0,0,0.5)50%), url("https://images.unsplash.com/photo-1488565546156-63ec9134f11e?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
/* Remove default padding */
[data-testid="stAppViewContainer"] {
    padding-top:;
}

/* Top navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: rgba(255, 255, 255, 0.1);
    padding: 1rem 2rem;
}
.navbar img {
    height: 40px;
}
.navbar button {
    background-color: white;
    color: black;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    cursor: pointer;
}

/* Hero section */
.hero {
    text-align: center;
    padding: 10px 0;
    background-color: rgba(255,255,255,0.1);
    color: white;
}
.hero h1 {
    font-size: 2.5rem;
    font-weight: bold;
}
.hero h1 span {
    color: #4285F4; /* Blue text */
}
.hero p {
    font-size: 1.2rem;
    margin-top: 1rem;
}
.hero .cta {
    margin-top: 2rem;
}
.hero .cta button {
    background-color: white;
    color: black;
    padding: 0.8rem 1.5rem;
    font-size: 1rem;
    border-radius: 8px;
    border: none;
    cursor: pointer;
}

/* Image gallery */
.gallery {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 1rem;
    padding: 2rem;
    background-color: rgba(255,255,255,0.1);
}
.gallery img {
    width: 300px;
    height: 200px;
    object-fit: cover;
    border-radius: 12px;
}
/* Login form */
.login-box {
    max-width: 400px;
    margin: 2rem auto;
    padding: 2rem;
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "home"


# --- Navbar ---
# --- Navbar ---


# --- Page rendering ---
#if st.session_state.page == "home" and not st.session_state.logged_in:
#  st.title("Welcome to Tripzy")
# st.write("Plan your perfect trip with us!")
    

    st.markdown("""
    <div class="navbar">
        <img src="https://images.squarespace-cdn.com/content/v1/6782a59d9f2e5a4d12afac77/bb8839f8-a268-42c0-8a9f-37b6e30dc7b7/Logo+final.PNG" alt="Logo">
        <div class="cta">
            <a href="http://localhost:8503/#login" target="_self">
            <button>Sign In →</button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Hero Section ---
    st.markdown("""
    <div class="hero">
        <h1>Travel with ease,with <span>Tripzy</span></h1>
        <p>Your Write any trip description here.</p>
        <div class="cta">
            <a href="http://localhost:8505/#share-your-travel-preferences" target="_self">
            <button>Plan a Trip</button>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Gallery ---
    st.markdown("""
    <div class="gallery">
        <img src="https://images.unsplash.com/photo-1626198226928-617fc6c6203e?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Tramp">
        <img src="https://images.unsplash.com/photo-1600080077823-a44592513861?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Victoria Memorial">
        <img src="https://images.unsplash.com/photo-1571679654681-ba01b9e1e117?q=80&w=1074&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="howrah bridge">

    </div>
    """, unsafe_allow_html=True)
    
