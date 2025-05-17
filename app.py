import streamlit as st

# Must be first
st.set_page_config(page_title="NLP Text Analytics Table", layout="centered")

import pandas as pd
import re
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob

# Downloads
nltk.download('punkt')
nltk.download('stopwords')

# Load NLP tools
@st.cache_resource
def load_spacy_model():
    return spacy.load("en_core_web_sm")

nlp = load_spacy_model()
stop_words = set(stopwords.words('english'))

# Core NLP functions
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

def extract_entities(text):
    doc = nlp(text)
    return ", ".join([ent.text for ent in doc.ents]) or "None"

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Initialize or load session data
if "data" not in st.session_state:
    example_data = [
        {"Text": "I love the new camera I bought from Amazon!", "Source": "Amazon Review"},
        {"Text": "Worst service ever. Not coming back! #disappointed", "Source": "Twitter"},
        {"Text": "Enjoying the sunset at Bali 🌅", "Source": "Instagram"},
        {"Text": "The product stopped working after 2 days.", "Source": "Amazon Review"},
        {"Text": "Just met Elon Musk at the conference!", "Source": "Twitter"},
        {"Text": "Unboxing the new iPhone 15 Pro Max!", "Source": "YouTube"},
    ]

    processed = []
    for entry in example_data:
        text = entry["Text"]
        processed.append({
            "Text": text,
            "Source": entry["Source"],
            "Entities": extract_entities(text),
            "Sentiment": get_sentiment(text)
        })

    st.session_state.data = processed

# UI
st.title("📊 NLP Text Analytics Table")

# New Entry Section
st.subheader("➕ Add New Entry")
new_text = st.text_area("Enter comment or review:")
new_source = st.selectbox("Select Source", ["Instagram", "Twitter", "Amazon Review", "YouTube", "Other"])

if st.button("Add to Table"):
    if new_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        st.session_state.data.append({
            "Text": new_text,
            "Source": new_source,
            "Entities": extract_entities(new_text),
            "Sentiment": get_sentiment(new_text)
        })
        st.success("Entry added to the table!")

# Display Table
st.subheader("📋 All Entries")
df = pd.DataFrame(st.session_state.data)
st.dataframe(df, use_container_width=True)
