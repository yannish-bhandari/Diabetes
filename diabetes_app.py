import streamlit as st
from home import main as home_main
from prediction import main as prediction_main

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction"])

# Render the appropriate page
if page == "Home":
    home_main()
elif page == "Prediction":
    prediction_main()
