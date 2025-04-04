import streamlit as st

pages = {
    "Go to": [
        st.Page("home.py", title="Home", icon="🏠"),
        st.Page("bmiTracker.py", title="BMI Tracker", icon="📏"),
        st.Page("workoutLogger.py", title="Workout Logger", icon="💪"),
        st.Page("progressTracker.py", title="Progress Tracker", icon="📈"),
    ],
}

pg = st.navigation(pages)
pg.run()