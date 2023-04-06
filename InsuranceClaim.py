# import tensorflow as tf
from sklearn.preprocessing import StandardScaler

import pickle
import streamlit as st

model = pickle.load('neural_model.pkl')
scaler= pickle.load('Scaler.pkl')
print(model)
print("here i am")
