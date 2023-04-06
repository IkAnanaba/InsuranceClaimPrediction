import tensorflow as tf
from sklearn.preprocessing import StandardScaler
 
import pickle
import streamlit as st

pickles = {'scaler': ['scaler.pkl'], 'encoders': ['encoders.pkl']}
model = tf.keras.models.load_model('neural_model')

for pkl in pickles:
    with open(pickles[pkl][0], "rb") as pkl_file:
        pickles[pkl][0] = pickle.load(pkl_file)



st.title('Are you liable for an insurance claim?')

YearOfObservation = st.number_input('Year propery was observed',  min_value=2013.00, max_value=2016.00, step=1.00)

YearOfOccupancy = st.number_input('Year of Occupancy',  min_value=2000.00, max_value=2016.00, step=1.00)

InsuredPeriod = st.slider('Buidling insurance period [Full Year = 1, 6 months = 0.5]', 0, 1)

Residential = st.checkbox('Residential')

BuildingPainted = st.checkbox('Is painted')

BuildingFenced = st.checkbox('Is fenced')

Garden = st.checkbox('Has a Garden')

Settlement = st.checkbox('Settlement')

BuildingDimension = st.number_input('Square Meter area of the building', min_value=1, max_value=30745, step=1.0)

BuildingType = st.selectbox('Building Type', ['1', '2', '3', '4'])

