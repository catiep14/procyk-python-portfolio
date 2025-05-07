```
# 📰 Fake News Analyzer – Streamlit App

## 📌 Project Overview

Fake news is a major issue in today's information ecosystem, spreading rapidly through social media and online platforms. This Streamlit app provides an interactive way to explore and analyze fake vs. real news articles using Natural Language Processing (NLP) and machine learning.

By training a model on labeled news datasets, users can:
- Explore real vs. fake news samples
- Train a classification model
- Test custom input to detect whether it's likely **real** or **fake**

---

## ⚙️ Setup & Run Instructions

### 🔧 Requirements

Make sure you have Python 3.7+ installed. Then install the following dependencies:

```bash
pip install -r requirements.txt
```

### 📄 `requirements.txt`

```text
streamlit==1.33.0
pandas==2.2.1
matplotlib==3.8.4
seaborn==0.13.2
scikit-learn==1.4.2
wordcloud==1.9.3
joblib==1.4.0
```

### 🚀 To Run the App Locally

1. Clone this repository or download the files.

```bash
git clone https://github.com/yourusername/FakeNewsAnalyzer.git
cd FakeNewsAnalyzer
```

2. Launch the Streamlit app:

```bash
streamlit run app.py
```

> 📁 The app will automatically generate `True_sample.csv` and `Fake_sample.csv` if missing.

---

## 🧠 App Features

### 📊 **Explore Data**
- View distribution of REAL vs FAKE news
- Pie chart and bar chart visualization
- Generate word clouds by class

### 🤖 **Train & Predict**
- Preprocesses news data using TF-IDF vectorization
- Trains a logistic regression model on the combined dataset
- Shows a classification report (precision, recall, F1-score)

### 📝 **Try Your Own**
- Input your own article or headline
- Predict whether it's real or fake
- Displays result with visual feedback (🟢 Real / 🔴 Fake)

---

## 📚 References & Resources

- Dataset: [Real and Fake News on Kaggle](https://www.kaggle.com/datasets/razanaqvi14/real-and-fake-news)
- Streamlit Docs: [https://docs.streamlit.io](https://docs.streamlit.io)
- scikit-learn Docs: [https://scikit-learn.org](https://scikit-learn.org)
- WordCloud: [https://amueller.github.io/word_cloud/](https://amueller.github.io/word_cloud/)

---

## 🖼️ Visual Examples

### Class Distribution (Bar + Pie Chart)
![Bar Chart](screenshots/bar_chart.png)
![Pie Chart](screenshots/pie_chart.png)

### Word Cloud Example
![WordCloud](screenshots/wordcloud_real.png)

### Prediction Output
![Prediction](screenshots/prediction_real.png)

---

## 📁 Project Structure

```
StreamlitAppFinal/
│
├── app.py                  # Main Streamlit App
├── True_sample.csv         # Sample real news data (auto-generated)
├── Fake_sample.csv         # Sample fake news data (auto-generated)
├── requirements.txt
├── README.md
└── screenshots/
    ├── bar_chart.png
    ├── pie_chart.png
    ├── wordcloud_real.png
    └── prediction_real.png
```