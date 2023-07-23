import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# Define the deep learning model architecture
def create_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(5, activation='relu', input_shape=(5,)))
    model.add(tf.keras.layers.Dense(5, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def stress_prediction(input_data):
    # Load the model using the custom architecture function
    model = create_model()
    model.load_weights('NN_model.h5')

    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = model.predict(input_data_reshaped)
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
        prediction = int(prediction)
        st.success(f"Stress Level: {prediction}")

if __name__ == '__main__':
    main()
