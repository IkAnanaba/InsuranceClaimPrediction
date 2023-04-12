import tensorflow as tf
from sklearn.preprocessing import StandardScaler
 
import pickle
import streamlit as st
import pandas as pd
import numpy as np

model = tf.keras.models.load_model('neural_model')

with open('Scaler.pkl', "rb") as pkl_file:
        scaler = pickle.load(pkl_file)

def transform(dataFrame):
    df = dataFrame.copy()
    df['Garden'] = df['Garden'].apply(lambda x: int(x))
    df['Residential'] = df['Residential'].apply(lambda x: int(x))
    df['Building_Painted'] = df['Building_Painted'].apply(lambda x: int(x))
    df['Building_Fenced'] = df['Building_Fenced'].apply(lambda x: int(x))
    df['Settlement'] = df['Settlement'].apply(lambda x: int(x))
    df['Building_Type'] = df['Building_Type'].apply(lambda x: int(x))
    
    return df

def scale(dataFrame):
    df = dataFrame.copy()
    df = scaler.transform(df)
    return df

st.title('Are you liable for an insurance claim?')

YearOfObservation = st.number_input('Year propery was observed',  min_value=2013.00, max_value=2016.00, step=1.00)

YearOfOccupancy = st.number_input('Year of Occupancy',  min_value=2000.00, max_value=2016.00, step=1.00)

InsuredPeriod = st.slider('Buidling insurance period [Full Year = 1, 6 months = 0.5]', max_value=0.00, min_value=1.00, step=0.01)

Residential = st.checkbox('Residential')

BuildingPainted = st.checkbox('Is painted')

BuildingFenced = st.checkbox('Is fenced')

Garden = st.checkbox('Has a Garden')

Settlement = st.checkbox('Settlement')

BuildingDimension = st.number_input('Square Meter area of the building', min_value=1.00, max_value=30745.00, step=1.00)

BuildingType = st.selectbox('Building Type', ['1', '2', '3', '4'])

if st.button('Get your result'):
    data = {'YearOfObservation': YearOfObservation,
            'Insured_Period': InsuredPeriod,
            'Residential': Residential,
            'Building_Painted': BuildingPainted,
            'Building_Fenced': BuildingPainted,
            'Garden' : Garden,
            'Settlement' : Settlement,
            'Building Dimension' : BuildingDimension,
            'Building_Type' : BuildingType,
            'Date_of_Occupancy': YearOfOccupancy}
    data_frame = pd.DataFrame(data, index=[0])

    data_frame = transform(data_frame)
    data_frame = scale(data_frame)

    st.write(data_frame)
    st.write(model.predict(data_frame))

