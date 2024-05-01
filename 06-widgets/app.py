import streamlit as st
import pandas as pd
import numpy as np


x = st.slider("x")
st.write(x, "squared is ", x*x)

st.divider()

st.write("Displaying text input")
input = st.text_input("Enter your name", key="name")

if input:
    st.write("Hello ", st.session_state.name)
    # st.write("Hello", input)


st.divider()

st.write("Displaying the use of checkbox")

show_dataframe = st.checkbox("Show dataframe")
show_map = st.checkbox("Show map")

if show_dataframe:
    chart_data = pd.DataFrame(
        np.random.randn(10, 3),
        columns=["a", "b", "c"]
    )

    chart_data

if show_map:
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [5.614818, -0.205874],
        columns=["lat", "lon"]
    )

    st.map(
        map_data,
        color="#ffaa0088"
    )