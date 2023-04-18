from sklearn.metrics.pairwise import cosine_similarity

# TBD Define an only function for the two kinds of embeddings

def euclidean_word2vec(word1, word2, nlp):

    # Compute the distance between the two vector embeddings
    similarity = cosine_similarity(word1.reshape(1, -1), word2.reshape(1, -1))

    return similarity[0][0]