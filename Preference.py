import streamlit as st

# Page configuration
st.set_page_config(page_title="Preferences", page_icon="🌍", layout="centered")

# Background + Card CSS
page_bg_img = """
<style>
/* Background Image */
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(to top, rgba(0,0,0,0.5)50%,rgba(0,0,0,0.5)50%),url("https://images.unsplash.com/photo-1669315576090-405ef98113c1?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Remove default header background */
[data-testid="stHeader"] {
    #background: transparent;
}

/* Card Styling */
.card {
    background: rgba(0, 0, 0, 0.75);
    padding: 60px;
    border-radius: 50px;
    max-width: 900px;
    margin: auto;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}
/* Centered Card Content */
.card h1 {
    text-align: center;
    color: white;
}


/* White Text Everywhere */
h1, h2, h3, h4, p, label, span {
    color: offwhite;
    border-radius: 100px;
}



.stRadio > div {
    background-color: rgba(255,255,255,0.1);
    padding: 10px;
    border-radius: 10px;
}

.stButton > button {
    background-color: #4285F4;
    color: white;

</style>
"""

# Apply CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Centered card content
with st.container():
    #st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Share Your Travel Preferences</h1>", unsafe_allow_html=True)
    st.write("Embark on your dream adventure with just a few simple details. **Tripzy** will curate a personalized itinerary, crafted to match your unique preferences!")

    # Location input
    #location = st.text_input("Where do you want to Explore? 🏖️", placeholder="Enter a location")

    # Trip duration
    trip_length = st.number_input("How long is your Trip? ⏰", min_value=1, step=1, placeholder="Ex: 2")

        # Budget
    budget = st.selectbox("What is your Budget? 💳", ["Low", "Medium", "High"])

        # Travel companion
    st.write("Who are you traveling with? 🚗")
    travel_with = st.radio(
        "",
        ["🧍 Solo - Discovering on Your Own (1 Person)", "💑 Partner - Exploring with a Loved One", "👨‍👩‍👧 Family - Traveling with Family", "👯 Friends - Exploring with Friends"]
        )

        # Submit button
    if st.button("Submit"):
        st.success(f" budget ₹{budget}, traveling with {travel_with}.")

    st.markdown("</div>", unsafe_allow_html=True)