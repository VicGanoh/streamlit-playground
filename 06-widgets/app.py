import streamlit as st


x = st.slider("x")
st.write(x, "squared is ", x*x)

st.divider()

st.write("Displaying text input")
input = st.text_input("Enter your name", key="name")

if input:
    st.write("Hello ", st.session_state.name)