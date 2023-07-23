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
    st.sidebar.markdown("### Practices to Relax Stress")
    st.sidebar.write("""
- Deep Breathing: Practice deep breathing exercises to calm the nervous system and reduce stress levels. Take slow, deep breaths, hold briefly, and then exhale slowly.
- Meditation: Engage in mindfulness meditation to focus your mind on the present moment and let go of stressful thoughts.
- Progressive Muscle Relaxation: Tense and then relax each muscle group in your body, starting from your feet up to your head, to release physical tension.
- Yoga: Participate in yoga classes or follow guided yoga sessions to improve flexibility, relieve tension, and promote relaxation.
- Exercise: Regular physical activity, such as walking, jogging, or swimming, can help release endorphins and reduce stress.

- Spending Time in Nature: Take a walk in the park, hike, or simply spend time outdoors to connect with nature and promote a sense of calm.

- Journaling: Write down your thoughts, feelings, and worries in a journal to gain clarity and release emotional tension.

- Reading: Escape into a good book or engage in literature that interests you to take your mind off stressors.

- Creative Outlets: Engage in creative activities like drawing, painting, crafting, or playing a musical instrument to express yourself and unwind.

- Listening to Music: Listen to soothing music or your favorite tunes to relax and uplift your mood.

- Socializing: Spend quality time with friends and loved ones to share experiences and receive emotional support.

- Laughter: Watch a comedy show or engage in activities that make you laugh, as laughter can release endorphins and reduce stress.

- Aromatherapy: Use essential oils like lavender, chamomile, or eucalyptus to promote relaxation and reduce stress.

- Limiting Screen Time: Reduce exposure to screens (phones, computers, TVs) before bedtime to improve sleep quality and reduce stress.

- Mindful Eating: Pay attention to your meals, savoring each bite and eating healthy, balanced foods that nourish your body.

- Warm Baths: Take a warm bath with Epsom salts or essential oils to soothe your muscles and calm your mind.

- Visualization: Imagine yourself in a peaceful and serene place to evoke relaxation responses.

- Mindful Walking: Practice walking meditation, paying attention to each step and your surroundings.

- Disconnect: Take a break from technology and social media to reduce mental clutter and promote relaxation.

- Seek Professional Help: If stress becomes overwhelming or chronic, don't hesitate to seek support from a mental health professional or counselor.
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
