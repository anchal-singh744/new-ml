import streamlit as st
from PIL import Image

def app():
    st.markdown("""

    # PROJECT PHASE - Sem VI

    ## Emotion text Classification using NLP and Machine Learning by Anchal Singh and Team


    """)

    # image = Image.open('images/speech-text.png')
    image = Image.open('images/nlp_home.png')
    st.image(image)

    st.markdown("""
    Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. The goal is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves.
    """)

    

    st.markdown("""
    ## Find Us
    ##### Anchal Singh  ( https://github.com/anchal-singh744/ )
    """)
