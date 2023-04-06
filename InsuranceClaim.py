import tensorflow as tf
from sklearn.preprocessing import StandardScaler
 
import pickle
import streamlit as st

pickles = {'scaler': ['scaler.pkl'], 'encoders': ['encoder.pkl']}
model = tf.keras.models.load_model('neural_model')

for pkl in pickles:
    with open(pickles[pkl][0], "rb") as pkl_file:
        pickles[pkl][1] = pickle.load(pkl_file)

print(pickles)
print("here i am")
