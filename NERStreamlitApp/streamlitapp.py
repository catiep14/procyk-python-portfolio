import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import pandas as pd

# Colors 
st.markdown("""
    <style>
    .stApp { background-color: #fef9f4; font-family: 'Helvetica', sans-serif; }
    [data-testid="stSidebar"] { background-color: #e6f2ff; }
    .stTextInput > div > div > input,
    .stTextArea > div > textarea {
        background-color: #f3e6ff;
        color: #333333;
        border-radius: 8px;
    }
    .stButton button {
        background-image: linear-gradient(to right, #a1c4fd, #c2e9fb);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-image: linear-gradient(to right, #89f7fe, #66a6ff);
        color: white;
    }
    .entities {
        background: #fffbd5;
        padding: 1.5rem;
        border-radius: 16px;
        margin-top: 1rem;
        border: 1px solid #ffe299;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #ff6f91;
    }
    </style>
""", unsafe_allow_html=True)

#spaCy setup
nlp = spacy.blank("en")
if "ruler" not in nlp.pipe_names:
    nlp.add_pipe("entity_ruler")
ruler = nlp.get_pipe("entity_ruler")

#Harry Potter NER patterns
harry_potter_patterns = {
    "CHARACTER": ["Harry Potter", "Hermione Granger", "Ron Weasley", "Albus Dumbledore", "Severus Snape"],
    "HOUSE": ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"],
    "SPELL": ["Expelliarmus", "Avada Kedavra", "Wingardium Leviosa", "Expecto Patronum"],
    "LOCATION": ["Hogwarts", "Diagon Alley", "Hogsmeade", "Azkaban", "Forbidden Forest"],
    "CREATURE": ["Hippogriff", "Dementor", "Basilisk", "House-elf"],
    "OBJECT": ["Invisibility Cloak", "Marauder’s Map", "Horcrux", "Time-Turner"]
}

#Title and sidebar
st.title("🧙 Custom NER: Harry Potter Edition")
st.sidebar.header("🔮 Choose Entity Types")

selected_labels = st.sidebar.multiselect(
    "Select entity types to apply:",
    options=list(harry_potter_patterns.keys()),
    default=["CHARACTER", "SPELL"]
)

# Add selected patterns to spaCy ruler
ruler.clear()
for label in selected_labels:
    patterns = [{"label": label, "pattern": name} for name in harry_potter_patterns[label]]
    ruler.add_patterns(patterns)

# Text input
st.subheader("📝 Input Text")
sample_text = (
    "Harry Potter and Hermione Granger used the Marauder’s Map to find their way around Hogwarts. "
    "They saw a Hippogriff in the Forbidden Forest. Ron Weasley shouted 'Wingardium Leviosa!' "
    "as they fled from a Dementor near the edge of Hogsmeade."
)
input_mode = st.radio("Choose input method:", ["Use Sample", "Write Text", "Upload File"])

if input_mode == "Use Sample":
    text = sample_text
    st.code(text, language="markdown")
elif input_mode == "Write Text":
    text = st.text_area("Enter your magical story:", height=200)
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")
    else:
        text = ""

# Process and Display
if text:
    doc = nlp(text)
    st.subheader("✨ Detected Entities")
    st.markdown(
        f"<div class='entities'>{displacy.render(doc, style='ent', jupyter=False)}</div>",
        unsafe_allow_html=True
    )

    # Entity list
    ents_data = [{"Text": ent.text, "Label": ent.label_} for ent in doc.ents]
    if ents_data:
        st.subheader("📋 Entity Summary")
        st.dataframe(pd.DataFrame(ents_data))
    else:
        st.info("No magical entities found.")
