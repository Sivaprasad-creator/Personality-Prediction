# step 1 : import libraries

import joblib
import pandas as pd
import streamlit as st

# step 2 : load saved model

model = joblib.load('personality_prediction.pkl')
encoder = model['label_encoder']
pipeline = model['pipeline']

# step 3 : user input

st.title("Personality Prediction")

time = st.selectbox("Time Spend Alone", ["--- Select Time Spend Alone ---", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
stage = st.selectbox("Stage Fear", ["--- Select Stage Fear ---", 'Yes', 'No'])
social = st.selectbox("Social Event Attendence", ["--- Select Social Event Attendece ---", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
going = st.selectbox("Going Outside", ["--- Select Going Outside ---", 0, 1, 2, 3, 4, 5, 6, 7])
drained = st.selectbox("Drained After Socializing", ["--- Select Drained After Socializing ---", 'Yes', 'No'])
friend = st.selectbox("Friend Circle Size", ["--- Select Friend Circle Size ---", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
post = st.selectbox("Post Frequency", ["--- Select Post Frequency ---", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# step 4 : predcition

if st.button('Predict'):

    sample_date = pd.DataFrame([{
    'Time_spent_Alone' : time,
    'Stage_fear' : stage,
    'Social_event_attendance' : social,
    'Going_outside' : going,
    'Drained_after_socializing' : drained,
    'Friends_circle_size' : friend,
    'Post_frequency' : post
}])
    prediction = pipeline.predict(sample_date)
    label = encoder.inverse_transform(prediction)[0]

    if label == 'Introvert':
        st.error("The Person is an Introvert")
    else:
        st.sucess("The Person is an Extrovert")


