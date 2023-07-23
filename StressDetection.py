# -*- coding: utf-8 -*-
"""fyp2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l3LiZY2Dqbax6BmNy3LFo1qrwWYh059c
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
import tensorflow as tf
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
#from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
#from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
#from scikeras.wrappers import KerasClassifier
#from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

df = pd.read_excel('data.xlsx')
df

df.isna().sum().sum()

"""# PRE PROCESSING"""

df.replace(['Male','Female'],[0,1],inplace=True)
df.drop(['Time','ID'],axis=1,inplace=True)
df['Bmi'] = df['Weight (Kg)']/((df['Height (Cm)']/100)**2)
dfBmi = df.drop(['Weight (Kg)','Height (Cm)'],axis=1)
#dfBmi = dfBmi.fillna(dfBmi.median())
dfclean = dfBmi.dropna()

###################################################################
# filter out the outliers
Q1 = dfBmi['Temperature'].quantile(0.25)
Q3 = dfBmi['Temperature'].quantile(0.75)
IQR = Q3 - Q1


lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR


dfBmi = dfBmi[(dfBmi['Temperature'] >= lower_bound) & (dfBmi['Temperature'] <= upper_bound)]
dfBmi

"""# DF Clean is the Dataset Used Ignore the others"""

Q1 = dfclean['Temperature'].quantile(0.25)
Q3 = dfclean['Temperature'].quantile(0.75)
IQR = Q3 - Q1

# define the upper and lower bounds
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR

# filter out the outliers
dfclean = dfclean[(dfclean['Temperature'] >= lower_bound) & (dfclean['Temperature'] <= upper_bound)]
dfclean

dfclean.to_csv('dfclean.csv')

"""# Deep Learning with cross validation"""

# Split the dataset into features and labels
X = dfclean.drop('Label', axis=1).values
y = dfclean['Label'].values

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Define the deep learning model
def create_model():
    model = Sequential()
    model.add(Dense(5, activation='relu', input_shape=(X.shape[1],)))
    model.add(Dense(5, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Create the scikit-learn compatible Keras model
model = KerasClassifier(build_fn=create_model, epochs=10, batch_size=64, verbose=0)

# Perform cross-validation
num_folds = 5
cv = KFold(n_splits=num_folds, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

# Print the accuracy scores for each fold
print("Accuracy scores for each fold:", scores)

# Print the mean accuracy and standard deviation
print("Mean accuracy:", scores.mean())
print("Standard deviation:", scores.std())

# Fit the model on the entire dataset before saving
model.fit(X, y, epochs=10, batch_size=64, verbose=0)

# Get the underlying Keras model
keras_model = model.model

# Save the Keras model to a file
keras_model.save('NN_model.h5')

print("Model saved.")

import pickle
# saving the model
filename = 'trained_model.sav'
pickle.dump(keras_model, open(filename, 'wb'))

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

#!pip install streamlit

def stress_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    return prediction


# In[128]:Gender,Age,Temperature,Pulse rate,Label,Bmi


import streamlit as st
def main():
    st.title("stress prediction")
    Gender = st.text_input("Gender ")
    Age = st.text_input("Age ")
    Bmi = st.text_input("Bmi ")
    Temperature = st.text_input("Temperature ")
    Pulse_rate = st.text_input("Pulse rate ")

    #code for prediction
    condition = ''

    #creating a button for prediction
#Gender,Age,Bmi,emperature,Pulse_rate
    if st.button("Stress prediction"):
        condition=stress_prediction([Gender,Age,Bmi,emperature,Pulse_rate])

    st.success(condition)

if __name__ == '__main__':
    main()

#!streamlit run /usr/local/lib/python3.10/dist-packages/ipykernel_launcher.py

