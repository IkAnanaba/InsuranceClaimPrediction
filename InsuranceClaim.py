import tensorflow as tf
from sklearn.preprocessing import StandardScaler

import pickle
import streamlit as st

pickles = {'model': ['neural_model.pkl'], 'scaler': ['scaler.pkl'], 'encoder': ['encoder.pkl']}

for pkl in pickles:
    with open(pickles[pkl][0], "rb") as pkl_file:
        pickles[pkl][1] = pickle.load(pkl_file)

print(pickles)
print("here i am")
