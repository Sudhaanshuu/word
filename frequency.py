import json
import streamlit as st
import string
from collections import Counter
from streamlit_lottie import st_lottie
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
st.markdown("""# Word Analysis by Sudhanshu""")
lottie_code = load_lottiefile("file/code.json")
st_lottie(lottie_code, speed=1, reverse=False, loop=True,
          quality="low", height=350, key=None,)
text = st.text_input("Enter the text to be analyzed: ")
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()
stopwords = ["a", "an", "the", "is", "and", "in", "of", "on","to", "it", "with", "for", "are", "i.e", "it's", "for"]
words = [word for word in words if word.lower() not in stopwords]
word_freq = Counter(words)
st.success("Word Frequency Analysis:")
for word, freq in word_freq.items():
    st.write(f'{word}: {freq}')