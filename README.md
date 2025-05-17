# Enhance-Text-Analytics-NLP
A project to improve text analytics data quality using Natural Language Processing (NLP) with Jupyter and Streamlit.
📊 Enhanced Text Analytics Data Quality with NLP

This project develops a modular NLP pipeline and an interactive Streamlit app to improve text data quality — tackling noise, inconsistencies, bias, and lack of context in unstructured text from sources like reviews and social media.

🔍 Overview

In today’s data-centric world, the quality of text data heavily influences analytical outcomes. This project uses NLP to clean, normalize, enrich, and analyze text to improve downstream analytics such as sentiment detection and entity recognition.

---

🧠 Key Features

- Clean and normalize noisy text (lowercase, remove stopwords, correct spelling)
- Named Entity Recognition (NER) with spaCy
- Sentiment analysis using TextBlob
- Interactive Streamlit web app for live text entry and analysis
- Scalable and modular Python pipeline

---

🚀 Files Included

Project.ipynb  NLP pipeline in Jupyter with logging, preprocessing, and analysis
app.py Streamlit web app for real-time input and table-based analytics 
requirements.txt Python dependencies 


---

⚙️ Installation

```bash
git clone https://github.com/kumarDarshan01/Enhanced-Text-Analytics-NLP.git
cd Enhanced-Text-Analytics-NLP
pip install -r requirements.txt
python -m textblob.download_corpora
python -m spacy download en_core_web_sm
