```
# 📰 Fake News Analyzer – Streamlit App

## 📌 Project Overview

Fake news is a major issue in today's information ecosystem, spreading rapidly through social media and online platforms. This Streamlit app provides an interactive way to explore and analyze fake vs. real news articles using Natural Language Processing (NLP) and machine learning.

Post graduation, I will work in the public relations field, so media is a vital piece to how that industry functions

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
<img width="671" alt="Screenshot 2025-05-07 at 3 15 22 PM" src="https://github.com/user-attachments/assets/81f33d49-cc37-47ee-8a33-de4971f903b0" />

<img width="646" alt="Screenshot 2025-05-07 at 3 18 54 PM" src="https://github.com/user-attachments/assets/daae390c-0f62-4e09-8523-fc1dae2c8562" />


### Word Cloud Example
<img width="661" alt="Screenshot 2025-05-07 at 3 06 32 PM" src="https://github.com/user-attachments/assets/afef538c-779e-4675-9d2d-7d90e87e123f" />
<img width="651" alt="Screenshot 2025-05-07 at 3 06 25 PM" src="https://github.com/user-attachments/assets/cfe1d03f-4156-422c-8713-a689082bd151" />

### Training model 
<img width="669" alt="Screenshot 2025-05-07 at 3 06 52 PM" src="https://github.com/user-attachments/assets/1364cb0f-1a91-4720-99bb-3653183f157f" />


### Prediction Output
<img width="712" alt="Screenshot 2025-05-07 at 3 06 40 PM" src="https://github.com/user-attachments/assets/8eca8341-001a-4f9a-9444-2176e0fac013" />
<img width="731" alt="Screenshot 2025-05-07 at 3 37 05 PM" src="https://github.com/user-attachments/assets/4c103a19-a389-4b6e-afcf-524955935c7e" />
<img width="709" alt="Screenshot 2025-05-07 at 3 37 23 PM" src="https://github.com/user-attachments/assets/cde4e3b4-120c-4b48-8a13-cc9678f52d3c" />


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
