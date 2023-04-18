# !pip install spacy
# !python -m spacy download en_core_web_md 

import spacy

def load_nlp():

    # Load the pre-trained model
    nlp = spacy.load("en_core_web_md")

    return nlp


def compute_vord2vec(word, nlp):
    
    # Obtain the vector embeddings for the word
    try:
        embedding = nlp(word).vector
        return embedding
    except:
        return None
    