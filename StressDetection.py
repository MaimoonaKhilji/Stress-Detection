import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

def stress_prediction(input_data):
    loaded_model = load_model('trained_model.sav')
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0][0]

def main():
    st.title("Stress Prediction")
    Gender = st.text_input("Gender (0 for Male, 1 for Female)")
    Age = st.text_input("Age")
    Bmi = st.text_input("BMI")
    Temperature = st.text_input("Temperature")
    Pulse_rate = st.text_input("Pulse rate")

    if st.button("Stress Prediction"):
        input_data = [Gender, Age, Bmi, Temperature, Pulse_rate]
        prediction = stress_prediction(input_data)
        st.success(f"Stress Level: {prediction}")

if __name__ == '__main__':
    main()
