def get_good_movies(movies):
    good_movies = [movie for movie in movies if movie['IMDB_score'] > 5.5]
    return good_movies
movies = [
    {'title': 'Inception', 'IMDB_score': 8.8},
    {'title': 'Interstellar', 'IMDB_score': 8.6},
    {'title': 'The Dark Knight', 'IMDB_score': 9.0},
    {'title': 'The Shawshank Redemption', 'IMDB_score': 9.3},
    {'title': 'The Matrix', 'IMDB_score': 8.7}
]

good_movies = get_good_movies(movies)
print("Good movies:")
for movie in good_movies:
    print(movie['title'], '-', movie['IMDB_score'])