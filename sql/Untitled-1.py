# %%
import spacy
nlp = spacy.load("en_core_web_sm")
# Tokenization
text = "The quick brown fox doesn't jump over the lazy dog. Natural Language Processing is fascinating!"
doc = nlp(text)
print("\nTokenization:")
for token in doc:
    print(f"Token: {token.text}, Head: {token.head.text}, Lemma: {token.lemma_}, Morph: {token.morph}")
# spaCy processes tokens by breaking down text into words, punctuation, and contractions
# Punctuation marks (e.g., periods, commas) are treated as separate tokens
# Contractions like "doesn't" are split into "does" and "n't"

# Part-of-Speech Tagging
print("\nPOS Tagging:")
for token in doc:
    print(f"Token: {token.text}, POS: {token.pos_}, Tag: {token.tag_}")
# "quick": POS = ADJ (adjective)
# "jumps": POS = VERB (verb)
# "is": POS = AUX (auxiliary verb)
# POS tagging is useful for grammar checking, machine translation, and syntactic analysis

# Named Entity Recognition (NER)
ner_text = "Barack Obama was the 44th President of the United States. He was born in Hawaii."
ner_doc = nlp(ner_text)
print("\nNamed Entity Recognition:")
for ent in ner_doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
# Recognized entities: "Barack Obama" (PERSON), "44th" (ORDINAL), "United States" (GPE), "Hawaii" (GPE)
# "Barack Obama" is labeled as PERSON, and "Hawaii" as GPE (Geopolitical Entity)

# Experimentation
experiment_text = "Apple Inc. released the iPhone 15 in 2023."
experiment_doc = nlp(experiment_text)
print("\nExperimentation:")
for ent in experiment_doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")

# Answers in comments:
# - spaCy correctly identifies "Apple Inc." as ORG (organization) and "2023" as DATE
# - Modifications like typos might cause entities to be unrecognized or misclassified
# - Adding punctuation might not significantly affect named entities but can impact tokenization



