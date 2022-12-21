import requests
import streamlit as st
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Steve_Jobs"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
doc = nlp(text)
entities = [ent.text for ent in doc.ents]

# Count the frequency of each entity
entity_counts = {}
for entity in entities:
    if entity in entity_counts:
        entity_counts[entity] += 1
    else:
        entity_counts[entity] = 1

# Extract the entities and their counts into separate lists
labels = list(entity_counts.keys())
values = list(entity_counts.values())

# Create the bar chart
st.bar_chart(values, labels)
