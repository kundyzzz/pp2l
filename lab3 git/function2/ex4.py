def average_imdb_score(movies):
    total_score = sum(movie['IMDB_score'] for movie in movies)
    average_score = total_score / len(movies) if movies else 0
    return average_score

# Example usage:
movies = [
    {'title': 'Inception', 'IMDB_score': 8.8},
    {'title': 'Interstellar', 'IMDB_score': 8.6},
    {'title': 'The Dark Knight', 'IMDB_score': 9.0},
    {'title': 'The Shawshank Redemption', 'IMDB_score': 9.3},
    {'title': 'The Matrix', 'IMDB_score': 8.7}
]

print("Average IMDB score:", average_imdb_score(movies))