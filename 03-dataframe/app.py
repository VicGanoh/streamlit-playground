import streamlit as st
import pandas as pd

st.write("My attempt using data to create a table with streamlit:")

st.write(
    pd.DataFrame(
        {
            "Name": ["Daniel", "Eric", "Kojo", "Adams"],
            "Score": [10, 35, 40, 50]
        }
    )
)