import streamlit as st
import pandas as pd
import os.path
import datetime

file_name = "Workout.csv"
path = "./"
check_file = os.path.exists(file_name)

if check_file:  
    st.session_state['data'] = pd.read_csv(file_name)
elif 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=["Date", "Exercise", "Sets", "Reps", "Weight (kg)"])


with st.form("exercise_form", clear_on_submit=True):
    st.header("💪 Workout Logger")
    
    exercise_name = st.text_input("Exercise name", placeholder="Run", value="Run")
    exercise_sets = st.number_input("Sets", min_value=1)
    exercise_reps = st.number_input("Reps", min_value=1)
    exercise_weight = st.number_input("Weight (kg)", min_value=1)
    date = "2025-04-04"

    submit_button = st.form_submit_button("Log Workout")

    if submit_button:
        data_row = {
            "Date": date, 
            "Exercise": exercise_name,
            "Sets": exercise_sets,
            "Reps": exercise_reps,
            "Weight (kg)": exercise_weight,
        }
        # Guardamos los nuevos datos junto con nuestros datos
        st.session_state['data'] = pd.concat([st.session_state['data'], pd.DataFrame([data_row])], ignore_index=True)
        # Guardamos los datos en un fichero
        st.session_state['data'].to_csv(file_name, index=False)

st.subheader("🏆 Workout History")
st.write(st.session_state['data'])
