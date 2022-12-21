import spacy
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
nlp = spacy.load("en_core_web_sm")
url = "https://en.wikipedia.org/wiki/Steve_Jobs"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
doc = nlp(text)
entities = [ent.text for ent in doc.ents]
#print(entities)

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
plt.figure(figsize=(10, 5))
plt.bar(labels, values)
# Add a title and axis labels
plt.title("Entity Frequency")
plt.xlabel("Entity")
plt.ylabel("Frequency")

# Show the plot
plt.show()
