import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    return pd.read_csv(url)

df = load_data()

# Streamlit App
st.title("🐧 Palmer Penguins Explorer")
st.write("A simple Streamlit app to explore the Palmer Penguins dataset.")

# Sidebar Filters
species = st.sidebar.multiselect("Select Species:", df["species"].dropna().unique(), default=df["species"].dropna().unique())
bill_length = st.sidebar.slider("Bill Length (mm):", float(df["bill_length_mm"].min()), float(df["bill_length_mm"].max()), (float(df["bill_length_mm"].min()), float(df["bill_length_mm"].max())))

# Filter Data
filtered_df = df[(df["species"].isin(species)) & (df["bill_length_mm"].between(bill_length[0], bill_length[1]))]

# Display Data
st.write("### Filtered Data")
st.dataframe(filtered_df)
