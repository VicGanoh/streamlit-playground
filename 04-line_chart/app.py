import streamlit as st
import pandas as pd
import numpy as np

st.write("Sample Line chart with generated sample using numpy")

chart_data = pd.DataFrame(
    data=np.random.randn(10, 3),
    columns=["a", "b", "c"],
)

st.line_chart(chart_data)