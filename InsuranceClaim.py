import tensorflow as tf
from sklearn.preprocessing import StandardScaler
 
import pickle
import streamlit as st
import pandas as pd
import numpy as np

pickles = {'scaler': ['scaler.pkl'], 'encoders': ['encoders.pkl']}
model = tf.keras.models.load_model('neural_model')

for pkl in pickles:
    with open(pickles[pkl][0], "rb") as pkl_file:
        pickles[pkl][0] = pickle.load(pkl_file)

def transform(dataFrame):
    df = dataFrame.copy()
    df['Garden'] = df['Garden'].map({True: 'V', False: 'O'})
    df['Residential'] = df['Residential'].map({True:1, False: 0})
    df['Building_Painted'] = df['Building_Painted'].map({True:'N', False:'V'})
    df['Building_Fenced'] = df['Building_Fenced'].map({True:'N', False:'V'})
    df['Settlement'] = df['Settlement'].map({True:'R', False:'U'})
    df['Building_Type'] = df['Building_Type'].apply(lambda x: int(x))

    df['Garden'] = pickles['encoders']['Garden'].transform(df[['Garden']])
    df['Building_Fenced'] = pickles['encoders']['Building_Fenced'].transform(df[['Building_Fenced']])
    df['Building_Painted'] = pickles['encoders']['Building_Painted'].transform(df[['Building_Painted']])
    df['Settlement'] = pickles['encoders']['Settlement'].transform(df[['Settlement']])
    
    return df

def scale(dataFrame):
    df = dataFrame.copy()
    pickles['scaler'][0].fit(df)

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
            'Date_Of_Occupancy': YearOfOccupancy}
    data_frame = pd.DataFrame(data, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    data_frame = transform(data_frame)
    data_frame = scale(data_frame)

    st.write(model.predict(data_frame))

