import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import string
import re
import random

st.set_page_config(page_title="Fake News Analyzer", layout="wide")

st.title("📰 Real vs Fake News Analyzer")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff0000, #ffffff);
        color: #000;
    }
    .st-bx {
        background-color: #B22234 !important;
        border-radius: 8px;
        padding: 10px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    true_df = pd.read_csv("True.csv")
    fake_df = pd.read_csv("Fake.csv")
    true_df["label"] = "REAL"
    fake_df["label"] = "FAKE"
    df = pd.concat([true_df, fake_df], ignore_index=True)
    df.dropna(subset=["title", "text", "label"], inplace=True)
    return df

@st.cache_resource
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@w+|\#','', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

@st.cache_resource
def train_model(df):
    df['content'] = df['title'] + ' ' + df['text']
    df['content'] = df['content'].apply(clean_text)
    X = df['content']
    y = df['label'].apply(lambda x: 1 if x == "REAL" else 0)
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X_vec = vectorizer.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.3, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model, vectorizer, X_test, y_test

# Main UI
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .css-1v0mbdj {
        color: #B22234; /* red */
    }
    .st-bx {
        background-color: #3C3B6E; /* navy */
    }
    </style>
""", unsafe_allow_html=True)

tab = st.sidebar.radio("Choose Activity", ["📊 Explore Data", "🤖 Train & Predict", "📝 Try Your Own"])

df = load_data()

if tab == "📊 Explore Data":
    st.subheader("Class Distribution")

    class_counts = df['label'].value_counts()
    total = class_counts.sum()
    for label, count in class_counts.items():
        percent = (count / total) * 100
        st.write(f"**{label}**: {count} samples ({percent:.2f}%)")

    fig, ax = plt.subplots()
    sns.countplot(data=df, x='label', ax=ax, palette=['#B22234', '#3C3B6E'])
    st.pyplot(fig)

    st.subheader("Class Distribution (Pie Chart)")
    pie_labels = class_counts.index
    pie_sizes = class_counts.values
    fig2, ax2 = plt.subplots()
    ax2.pie(pie_sizes, labels=pie_labels, autopct='%1.1f%%', colors=['#B22234', '#3C3B6E'], startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig2)

    st.subheader("WordCloud")
    label = st.selectbox("Choose label to generate WordCloud", ["REAL", "FAKE"])
    text = ' '.join(df[df['label'] == label]['text'].astype(str).tolist())
    wc = WordCloud(width=800, height=400, background_color="white", colormap='coolwarm').generate(text)
    st.image(wc.to_array(), use_column_width=True)

elif tab == "🤖 Train & Predict":
    st.subheader("Model Training & Evaluation")
    model, vectorizer, X_test, y_test = train_model(df)
    y_pred = model.predict(X_test)
    st.text("Classification Report:")
    st.text(classification_report(y_test, y_pred))
    st.success("Model trained successfully!")

elif tab == "📝 Try Your Own":
    st.subheader("Test a News Article")
    model, vectorizer, _, _ = train_model(df)

    example_real_titles = df[df['label'] == "REAL"]['title'].dropna().tolist()
    random_title = random.choice(example_real_titles)
    st.markdown(f"**Example Real News Title:** _'{random_title}'_")

    user_input = st.text_area("Enter news text or title", height=200)
    if st.button("Check if Real or Fake"):
        if user_input:
            cleaned = clean_text(user_input)
            vec = vectorizer.transform([cleaned])
            pred = model.predict(vec)[0]
            st.markdown(f"<div class='st-bx'>{'🟢 Real News' if pred == 1 else '🔴 Fake News'}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter some text.")
