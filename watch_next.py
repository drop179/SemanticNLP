import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import spacy

nlp = spacy.load('en_core_web_md')  # Load pre-trained word embeddings

# Load the movies descriptions from the movies.txt file


def recommend_movie(input_description, movies_file):
    with open(movies_file) as f:
        movies = f.readlines()
    movies = [x.strip() for x in movies]

    # Convert movie descriptions into word vectors
    movie_vectors = [nlp(movie).vector for movie in movies]

    # Convert input description into a word vector
    input_vector = nlp(input_description).vector

    # Calculate similarity scores between the input vector and all movie vectors
    similarity_scores = cosine_similarity([input_vector], movie_vectors)[0]

    # Return the title of the movie with the highest similarity score
    most_similar_index = np.argmax(similarity_scores)
    return movies[most_similar_index]


input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
movies_file = "movies.txt"
recommended_movie = recommend_movie(input_description, movies_file)
print("Recommended movie:", recommended_movie)
