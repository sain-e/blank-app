import streamlit as st

st.header("Home Page")

comments = ["Stay strong!", "Step harder!", "They don't know me son!", "To the limits"]

for comment in comments:
    st.subheader(f"💪{comment}")

st.image("https://incrediwear.com/cdn/shop/articles/Lifting_Weights.jpg?v=1675195731", caption=None)

