import tensorflow as tf
from sklearn.preprocessing import StandardScaler
 
import pickle
import streamlit as st

pickles = {'scaler': ['scaler.pkl'], 'encoders': ['encoders.pkl']}
model = tf.keras.models.load_model('neural_model')

for pkl in pickles:
    with open(pickles[pkl][0], "rb") as pkl_file:
        pickles[pkl][0] = pickle.load(pkl_file)



st.title('See if your building is likely to have an insurance claim')

