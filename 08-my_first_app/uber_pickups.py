import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in NYC")


DATE_COLUMN = "date/time"

# Load data set
DATA_URL = ("https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz")

@st.cache_data
def load_data(nrows):
    """
    Load Uber pickups data from a URL.

    Parameters
    ----------
    nrows : int
        Number of rows of the data to read.

    Returns
    -------
    pd.DataFrame
        The read data.
    """
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(convert_to_lower, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

def convert_to_lower(x):
    return str(x).lower()

# Create a text element and let the reader know the data is loading.
data_load_state = st.text("Loading data...")

# Load 10,000 rows of data into the dataframe
data = load_data(10000)

# Notify the reader that the data was successfully loaded.
data_load_state.text("Loading data...done!")

st.divider()
st.subheader("Raw data")
