import streamlit as st
from src.predict import predict_performance

st.title("🎓 Student Performance Predictor")

study_hours = st.slider("Study Hours",0,10)
attendance = st.slider("Attendance (%)",0,100)
assignments = st.slider("Assignments Completed",0,10)
previous_score = st.slider("Previous Score",0,100)

if st.button("Predict"):

    result = predict_performance(
        study_hours,
        attendance,
        assignments,
        previous_score
    )

    st.success(f"Predicted Result: {result}")