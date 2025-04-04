import streamlit as st

st.header("📏 BMI Tracker")

user_height = st.number_input("Enter your height (cm)", min_value=1)
user_weight = st.number_input("Enter your weight (kg)", min_value=1)

if st.button("Calculate BMI"):
    result = user_weight / (user_height / 100) ** 2

    st.write(f"Your BMI is: {round(result, 2)}")

    st.write("✅BMI record saved!")

st.page_link("progressTracker.py", label="BMI Progress", icon="🐧")
