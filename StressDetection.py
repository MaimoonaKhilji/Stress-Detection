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

    # Create a sidebar for notes or additional content
    st.sidebar.markdown("### Notes")
    st.sidebar.write("""
### Practices to Relax Stress

- Deep Breathing: Practice deep breathing exercises to calm the nervous system and reduce stress levels. Take slow, deep breaths, hold briefly, and then exhale slowly.

- Meditation: Engage in mindfulness meditation to focus your mind on the present moment and let go of stressful thoughts.

- Progressive Muscle Relaxation: Tense and then relax each muscle group in your body, starting from your feet up to your head, to release physical tension.

- Yoga: Participate in yoga classes or follow guided yoga sessions to improve flexibility, relieve tension, and promote relaxation.

# Continue with other list items...
""")

    st.sidebar.write("You can use Markdown syntax to format the content.")

    # Main content on the left side
    Gender = st.text_input("Gender (0 for Male, 1 for Female)")
    Age = st.text_input("Age")
    Bmi = st.text_input("BMI")
    Temperature = st.text_input("Temperature")
    Pulse_rate = st.text_input("Pulse rate")

    if st.button("Stress Prediction"):
        input_data = [Gender, Age, Temperature, Pulse_rate, Bmi]
        prediction = stress_prediction(input_data)
        prediction = int(prediction)
        if prediction==1:
            result="No Stress"
        else:
            result="Stress Detected"
            st.write("Stress Detected! Playing Calm Sound...")
            calm_sound_path = 'Meydan-Freezing-but-warm.mp3'
            st.audio(calm_sound_path, format='audio/mp3')
        st.success(f"Stress Level: {result}")

    

if __name__ == '__main__':
    main()
