import streamlit as st
import pandas as pd
import numpy as np

st.write("My attempt using data to create a table with streamlit:")

st.write(
    pd.DataFrame(
        {
            "Name": ["Daniel", "Eric", "Kojo", "Adams"],
            "Score": [10, 35, 40, 50]
        }
    )
)

st.divider() # Draws a horizontal rule

st.write("Using numpy to generate random sample (10 by 20):")
dataframe = pd.DataFrame(
    data=np.random.randn(10, 20),
    columns=("col %d" % i for i in range(20))
)

st.write("This is an interactive table")
st.dataframe(dataframe.style.highlight_max(axis=0))

st.divider()

st.write("This is a static table:")
st.table(dataframe)
