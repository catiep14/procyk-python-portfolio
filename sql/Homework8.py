import spacy
import pandas as pd
from spacy.pipeline import EntityRuler
# Load a spaCy model so we can process the text
nlp = spacy.load("en_core_web_sm")
# Load the dataset
# Make sure the file is in the right location and that the path is correct
file_path = "stocks-1.tsv"  
df = pd.read_csv(file_path, sep='\t')
# Check dataframe to see what columns are available
# Shows where the company names and stock symbols are stored
print(df.head())  # Looks at the first few rows
# Take out unique company names and stock symbols
# Using unique values so we don’t make duplicate patterns, making the model more efficient overall
companies = df["Company Name"].unique().tolist()
stocks = df["Stock Symbol"].unique().tolist()
# Make patterns for the EntityRuler
patterns = []
# Instead of typing each company/stock manually, loop through them
for company in companies:
    patterns.append({"label": "COMPANY", "pattern": company})
for stock in stocks:
    patterns.append({"label": "STOCK", "pattern": stock})

# Add the EntityRuler to the NLP pipeline
# Before 'ner' because our rule-based matching happens before spaCy’s built-in entity recognition
ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(patterns)
# Define some test paragraphs containing company names and stock symbols
paragraphs = [
    "Helmerich & Payne (HP) saw its stock rise by 1.5%, fueled by optimistic forecasts in the Energy Equipment & Services sector...",
    "Aemetis (AMTX) saw its stock rise by 1.5%, fueled by optimistic forecasts in the Oil, Gas & Consumable Fuels sector...",
    "On a mixed trading day, Par Pacific Holdings (PARR) saw its stock rise by 1.5%, fueled by optimistic forecasts..."
]
# Test the EntityRuler and see if it correctly identifies the entities
for text in paragraphs:
    doc = nlp(text)
    print("Entities:")
    # Loops through detected entities and printing them
    for ent in doc.ents:
        print(f"{ent.text} - {ent.label_}")
    print("\n---\n")
