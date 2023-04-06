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

YearOfOccupancy = st.selectbox('Year of Occupancy',  min_value=2000.00, max_value=2016.00, step=1.00)

