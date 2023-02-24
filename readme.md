
# Movie Recommender Based on Word Vector Similarity

* This program is designed to recommend movies based on the similarity of their descriptions to a given input description. The system uses pre-trained word embeddings to convert the descriptions into word vectors and then calculates the cosine similarity between the input vector and all other movie vectors. The title of the movie with the highest similarity score is returned as the recommendation.

## Requirements
The program requires the following dependencies:

*Python 3.6 or higher*
*NumPy*
*Scikit-learn*
*spaCy*
Pre-trained word embeddings (such as en_core_web_md from spaCy)

## Installation
Clone the repository or download the code files.
Install the required dependencies using pip: pip install numpy scikit-learn spacy
Download the pre-trained word embeddings using python -m spacy download en_core_web_md

## Usage
1. Create a text file named movies.txt and add each movie description as a separate line.
2. Import the recommend_movie function from movie_recommender.py in your Python code.
3. Call the recommend_movie function with the input description and the path to the movies.txt file.
4. The function will return the title of the movie with the highest similarity score.

## Limitations
The quality of recommendations depends on the quality of the pre-trained word embeddings and the similarity metric used. The current implementation uses cosine similarity and the en_core_web_md word embeddings from spaCy, but other embeddings and metrics may perform differently.
The current implementation recommends only one movie based on the highest similarity score. A more sophisticated approach could recommend a list of top N movies or use a ranking system to prioritize recommendations based on multiple factors.
The current implementation does not take into account user preferences or history. A more personalized recommendation system could incorporate user feedback or behavior to improve recommendations.
