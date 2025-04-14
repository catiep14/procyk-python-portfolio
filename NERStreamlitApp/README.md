# 🧙‍♂️ Harry Potter NER App

A magical Named Entity Recognition (NER) app built with [spaCy](https://spacy.io/) and [Streamlit](https://streamlit.io/), featuring custom entity labels inspired by the Harry Potter universe! Detect characters, spells, creatures, and more using spaCy's `EntityRuler`.

---

## 📌 Project Overview

This app allows users to explore **Harry Potter Characters and Spells** through custom rules. Instead of relying solely on pre-trained models, we use **spaCy’s `EntityRuler`** to define rule-based entities — which works for custom domains like fantasy, fiction, or specialized technical fields.

In this version, we focus on **Harry Potter-themed labels** like `CHARACTER`, `SPELL`, and `LOCATION`, and highlight them in uploaded or written text using a colorful, easy-to-use interface.

---

## 🚀 Setup Instructions:

### ✅ Required Libraries

- `streamlit`
- `spacy`
- `pandas`

Install them using:

```bash
pip install streamlit spacy pandas
```

### ▶️ Running the App Locally

Clone this repo and run:

```bash
streamlit run streamlitapp.py
```

> Make sure you're using Python 3.7 or higher.

---

## 🌟 App Features

### 🔡 Input Options
- Add in your own text
- Use the included Harry Potter sample
- Upload a `.txt` file

### 🧙 Custom Entity Labels
Choose from predefined Harry Potter patterns like:

- `CHARACTER`: `Harry Potter`, `Hermione Granger`, `Ron Weasley`
- `SPELL`: `Expelliarmus`, `Avada Kedavra`, `Wingardium Leviosa`
- `HOUSE`: `Gryffindor`, `Slytherin`, `Ravenclaw`, `Hufflepuff`
- `LOCATION`: `Hogwarts`, `Azkaban`, `Diagon Alley`
- `CREATURE`: `Hippogriff`, `Dementor`, `Basilisk`
- `OBJECT`: `Invisibility Cloak`, `Horcrux`, `Marauder’s Map`

### 🧠 EntityRuler
We use `EntityRuler` from spaCy to match exact terms defined in your custom dictionary of entities.

### 📊 Entity Output
- **Color-coded visual text highlighting** via spaCy’s `displacy`
- **Entity summary table** showing each recognized term and its label

---

## 🔗 References

- [spaCy Named Entity Recognition](https://spacy.io/usage/linguistic-features#named-entities)
- [spaCy EntityRuler Documentation](https://spacy.io/api/entityruler)
- [Streamlit Docs](https://docs.streamlit.io/)

---

## 📸 Visual Examples

> Add screenshots like the following to your `images/` folder and link them here.

**App Interface**

![App Interface](images/app_interface.png)

**Detected Entities Highlighted**

![Entities Highlighted](images/entities_output.png)

**Sidebar with Label Selection**

![Sidebar](images/sidebar_options.png)

---

## 🌐 Deployed Version

> Coming soon: [Link to deployed app here](#)

---

