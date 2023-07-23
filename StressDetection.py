import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

import requests

def fetch_thingspeak_data(channel_id, read_api_key, num_entries=1):
    url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json"
    params = {
        "api_key": read_api_key,
        "results": num_entries
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['feeds']
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def get():
    # Replace with your own ThingSpeak Channel ID and Read API Key
    channel_id = '2163528'
    read_api_key = "3QP7OZ4X07IWX53K"
    num_entries = 1  # Fetching only the last entry

    data = fetch_thingspeak_data(channel_id, read_api_key, num_entries)
    entry = data[0]  # Access the first (and only) entry in the list
    return entry

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

   

  #  st.sidebar.write("You can use Markdown syntax to format the content.")

    # Main content on the left side
    Gender = st.text_input("Gender (0 for Male, 1 for Female)")
    Age = st.text_input("Age")
    Bmi = st.text_input("BMI")
    if st.button("Get Data"):
        entry = get()
        pulse_rate = entry['field1']
        Pulse_rate = float(pulse_rate)
        temperature = entry['field2']
        Temperature = float(temperature)

        # Show the retrieved data in the form
        st.write("Pulse Rate:", Pulse_rate)
        st.write("Temperature:", Temperature)
        
    #Temperature = st.text_input("Temperature")
    #Pulse_rate = st.text_input("Pulse rate")
  #  entry= get()
  #  pulse_rate = entry['field1']
  #  Pulse_rate = float(pulse_rate)
  #  temperature = entry['field2']
  #  Temperature = float(temperature)

    if st.button("Stress Prediction"):
        input_data = [Gender, Age, Temperature, Pulse_rate, Bmi]
        prediction = stress_prediction(input_data)
        prediction = int(prediction)
        if prediction==0:
            result="No Stress"
            st.sidebar.markdown("### Stay Happy")
            st.sidebar.write("Stay Healthy")
          #  st.sidebar.empty()
           # st.info("No Stress Detected") 
        else:
            result="Stress Detected"
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
            
            - **Seek Professional Help:** If stress becomes overwhelming or chronic, don't hesitate to seek support from a mental health professional or counselor.
            """)
                
            st.write("Stress Detected! Playing Calm Sound...")
            calm_sound_path = 'Meydan-Freezing-but-warm.mp3'
            st.audio(calm_sound_path, format='audio/mp3')
        st.success(f"Stress Level: {result}")

    







if __name__ == '__main__':
    main()
