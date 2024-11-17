import streamlit as st
import pickle
import numpy as np

def main():

    # Load the saved model
    pickle_in = open('model_classifier.pkl', 'rb')
    classifier = pickle.load(pickle_in)


    # Define the app title
    st.markdown("<h1 style='text-align: center;'>Diabetes Prediction App</h1>", unsafe_allow_html=True)

    # Provide a description
    st.write("""
    This app uses a machine learning model to predict whether a person has diabetes or not.
    """)

    # Sample average values (replace these with the actual averages from your dataset)
    avg_values = {
        "glucose": 110,
        "blood_pressure": 100,
        "skin_thickness": 20.5,
        "insulin": 79.8,
        "bmi": 26,
        "diabetes_pedigree": 0
    }

    # Input fields for user to enter data
    st.header("Enter the following details:")


    pregnancies = st.slider("Number of Pregnancies", min_value=0, max_value=20, step=1)

    # Glucose Level
    if st.checkbox("Use average value for Glucose Level"):
        glucose = avg_values["glucose"]
    else:
        glucose = st.slider("Glucose Level", min_value=0.0, max_value=300.0, step=0.1)

    # Blood Pressure
    if st.checkbox("Use average value for Blood Pressure"):
        blood_pressure = avg_values["blood_pressure"]
    else:
        blood_pressure = st.slider("Blood Pressure (mm Hg)", min_value=0.0, max_value=200.0, step=0.1)

    # Skin Thickness
    if st.checkbox("Use average value for Skin Thickness"):
        skin_thickness = avg_values["skin_thickness"]
    else:
        skin_thickness = st.slider("Skin Thickness (mm)", min_value=0.0, max_value=100.0, step=0.1)

    # Insulin
    if st.checkbox("Use average value for Insulin Level"):
        insulin = avg_values["insulin"]
    else:
        insulin = st.slider("Insulin Level", min_value=0.0, max_value=1000.0, step=0.1)

    # BMI
    if st.checkbox("Use average value for BMI"):
        bmi = avg_values["bmi"]
    else:
        bmi = st.slider("Body Mass Index (BMI)", min_value=0.0, max_value=100.0, step=0.1)

    # Diabetes Pedigree Function
    if st.checkbox("No known family history of Diabetes"):
        diabetes_pedigree = avg_values["diabetes_pedigree"]
    else:
        diabetes_pedigree = st.slider("Diabetes Pedigree Function", min_value=0.0, max_value=5.0, step=0.01)


    age = st.slider("Age", min_value=0, max_value=120, step=1)

    # Display the final input values
    st.write("### Selected Values:")
    st.write(f"Pregnancies: {pregnancies}")
    st.write(f"Glucose: {glucose}")
    st.write(f"Blood Pressure: {blood_pressure}")
    st.write(f"Skin Thickness: {skin_thickness}")
    st.write(f"Insulin: {insulin}")
    st.write(f"BMI: {bmi}")
    st.write(f"Diabetes Pedigree Function: {diabetes_pedigree}")
    st.write(f"Age: {age}")

    # Button for final prediction
    if st.button("Predict"):
        # Prepare the input data as an array
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
        
        # Make a prediction using the loaded model

        prediction = classifier.predict(input_data)
        
        # Display the prediction result
        if prediction[0] == 1:
            st.write("**SORRY!!!** you have Diabetes. Get medical attention quick!!")
        else:
            st.write("**CONGRATULATIONS!!!** you don't have Diabetes!")