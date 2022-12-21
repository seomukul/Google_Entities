import streamlit as st
import wikipedia
import nltk
url = st.text_input("https://en.wikipedia.org/wiki/Steve_Jobs:")
page = wikipedia.page(url=url)
content = page.content
tokens = nltk.word_tokenize(content)
fdist = nltk.FreqDist(tokens)
common_words = fdist.most_common(20)
st.write("Most common words:", common_words)
