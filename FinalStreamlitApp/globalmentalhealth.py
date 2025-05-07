import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title("Global Mental Health Analysis")

# Sidebar for user inputs
st.sidebar.header("User Input Features")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# Load data
@st.cache
def load_data(file):
    data = pd.read_csv(file)
    return data

if uploaded_file:
    data = load_data(uploaded_file)
else:
    data = load_data("Mental_health_Depression_disorder_Data.csv")

# Display dataset
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# Data preprocessing
st.subheader("Data Preprocessing")
st.write("Checking for missing values...")
missing_values = data.isnull().sum()
st.write(missing_values[missing_values > 0])

# Drop rows with missing values
data_clean = data.dropna()
st.write("Data after dropping missing values:")
st.write(data_clean.shape)

# Visualization: Gender Distribution
st.subheader("Gender Distribution")
gender_counts = data_clean['Gender'].value_counts()
st.bar_chart(gender_counts)

# Visualization: Age Distribution
st.subheader("Age Distribution")
plt.figure(figsize=(10, 5))
sns.histplot(data_clean['Age'], bins=20, kde=True)
st.pyplot(plt)

# Visualization: Depression by Region
st.subheader("Depression by Region")
region_depression = data_clean.groupby('Region')['Depression'].mean()
st.bar_chart(region_depression)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
plt.figure(figsize=(10, 8))
sns.heatmap(data_clean.corr(), annot=True, cmap='coolwarm')
st.pyplot(plt)
