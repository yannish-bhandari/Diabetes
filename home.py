import streamlit as st

def main():
    # Center the title using HTML and CSS
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>DIABETES PREDICTION</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Center-align a single image
    st.image("path_to_your_image.jpg", use_column_width=True)


    # Overlay text below the images
    st.write("""
    Analyzing and building a prediction model for diabetes is 
    crucial to enable early detection and prevention, aiming to 
    reduce complications and improve the quality of life for individuals at risk.
    """)

    # Problem Presentation
    st.header("Project Overview")
    st.write("""
    The diabetes dataset, sourced from the National Institute of Diabetes and Digestive 
    and Kidney Diseases, focuses on females of Pima Indian heritage aged 21 and above. 
    It includes key medical variables such as glucose levels, BMI, insulin, blood pressure,
     and pregnancies, along with a target variable indicating diabetes presence. 
     This dataset provides a solid foundation for analyzing the relationship between medical 
     factors and diabetes onset.

    Building a prediction model using this dataset is crucial for early diabetes detection, 
    enabling timely interventions and better healthcare decisions. By leveraging machine learning, this project 
    aims to identify individuals at risk and reduce complications, showcasing the power of 
    data-driven solutions in addressing critical health challenges.
    """)
