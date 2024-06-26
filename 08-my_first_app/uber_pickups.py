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


if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

# Add Histogram
st.subheader("Number of pickups by hour")

hist_values = pd.DataFrame( {
    "Number of pickups": np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0],
    "Hour": list(range(0,24))
} 
    
)
st.bar_chart(hist_values, x="Hour", y="Number of pickups", use_container_width=True)


# Plotting data on map
hour = st.slider("hour", 0, 23, 17) # min: 0h, max: 23h, default: 17h
st.subheader(f"Map of all pickups at {hour}:00")
filtered_data = data[data[DATE_COLUMN].dt.hour == hour]
st.map(filtered_data)