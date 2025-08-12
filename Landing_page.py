import streamlit as st

# --- Page config ---
st.set_page_config(page_title="Trip", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
/* Remove default padding */
[data-testid="stAppViewContainer"] {
    padding-top: 0;
}

/* Top navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: black;
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
    padding: 4rem 2rem;
    background-color: black;
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
    background-color: black;
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
if st.session_state.page == "home" and not st.session_state.logged_in:
    st.title("Welcome to Tripzy")
    st.write("Plan your perfect trip with us!")
    

    st.markdown("""
    <div class="navbar">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo_TV_2015.png" alt="Logo">
        <button>Sign In →</button>
    </div>
    """, unsafe_allow_html=True)

    # --- Hero Section ---
    st.markdown("""
    <div class="hero">
        <h1>As you wish <span>Tripzy</span></h1>
        <p>Your Write any trip description here.</p>
        <div class="cta">
            <button>Plan a Trip</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Gallery ---
    st.markdown("""
    <div class="gallery">
        <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb" alt="Stonehenge">
        <img src="Victoria_Memorial_By_Saprativa.jpg" alt="Victoria Memorial">
        <img src="C:\\Users\\DELL\\Downloads\\WhatsApp Image 2025-08-11 at 23.26.10.jpeg" alt="howrah bridge">

    </div>
    """, unsafe_allow_html=True)
    
