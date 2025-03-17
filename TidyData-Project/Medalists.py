
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit app title
st.title('Olympics 2008 Medalists Data Cleaning & Visualization')

# Load the dataset
file_path = 'olympics_08_medalists.csv'
df = pd.read_csv(file_path)

# Display raw data
st.subheader('Raw Data Preview')
st.write(df.head())

# Check for missing values
st.subheader('Missing Values')
st.write(df.isnull().sum())

# Print column names for debugging
st.subheader('Column Names in Dataset')
st.write(df.columns.tolist())

# Define identifier and event columns
id_var = 'medalist_name'
event_columns = [col for col in df.columns if col != id_var]  # Everything except the medalist name

# Reshape dataset (Melt)
df_melted = df.melt(id_vars=[id_var], var_name='Event', value_name='Medalist')

# Clean up event names
df_melted['Event'] = df_melted['Event'].str.replace('_', ' ').str.title()
df_melted.dropna(inplace=True)

# Display cleaned data
st.subheader('Cleaned Data Preview')
st.write(df_melted.head())

# Pivot Table: Count of medals per event
medal_counts = df_melted.groupby('Event').count()[['Medalist']].rename(columns={'Medalist': 'Medal Count'})

st.subheader('Medal Count by Event')
st.write(medal_counts.sort_values(by='Medal Count', ascending=False))

# Visualization 1: Top 10 Events by Medal Count
fig, ax = plt.subplots(figsize=(12,6))
medal_counts.nlargest(10, 'Medal Count').plot(kind='bar', legend=False, ax=ax)
ax.set_title('Top 10 Events by Medal Count')
ax.set_ylabel('Number of Medals')
ax.set_xlabel('Event')
plt.xticks(rotation=90)
st.pyplot(fig)

# Visualization 2: Medal distribution per sport category
fig, ax = plt.subplots(figsize=(12,6))
sns.countplot(data=df_melted, y='Event', order=df_melted['Event'].value_counts().index, ax=ax)
ax.set_title('Medal Distribution by Sport')
ax.set_xlabel('Number of Medals')
ax.set_ylabel('Sport')
st.pyplot(fig)

# Save cleaned dataset
df_melted.to_csv('cleaned_olympics_08_medalists.csv', index=False)
st.success('Cleaned dataset saved successfully!')
