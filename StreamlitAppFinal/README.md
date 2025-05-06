# SleepTrack Insight 🛌📊

## Project Overview
**SleepTrack Insight** is a Streamlit web app designed to help users better understand their sleep habits and patterns. By uploading simple CSV files that contain sleep tracking data (e.g., sleep duration, quality, bed/wake times), users can interactively visualize trends, filter by time periods, and uncover insights into their sleep behavior. The app promotes self-awareness and supports better sleep hygiene decisions.

---

## Features

🔹 **Upload Your Data**:  
Upload a CSV file with your sleep logs (e.g., from Apple Health, Google Fit, Oura, or manual tracking).

🔹 **Date Filtering**:  
Select a custom date range to explore specific periods of sleep behavior.

🔹 **Key Metrics Summary**:  
See average sleep duration, average sleep quality, and total days tracked.

🔹 **Interactive Visualizations**:  
- Line chart of sleep duration over time  
- Bar chart of sleep quality  
- Box plot showing variability in sleep duration  

🔹 **Error Handling & User Guidance**:  
Built-in messaging for unsupported file types, missing columns, and other upload issues.

---

## Example CSV Format

Your CSV should include at least the following columns:

```csv
date,sleep_duration,sleep_quality
2025-01-01,7.5,8
2025-01-02,6.8,7
2025-01-03,8.2,9
...
