def average_imdb_score_by_category(category, movies):
    category_movies = [movie['IMDB_score'] for movie in movies if movie['category'] == category]
    if not category_movies:
        return 0  # Return 0 if there are no movies in the specified category
    average_score = sum(category_movies) / len(category_movies)
    return average_score

# Example usage:
movies = [
    {'title': 'Inception', 'category': 'Sci-Fi', 'IMDB_score': 8.8},
    {'title': 'Interstellar', 'category': 'Sci-Fi', 'IMDB_score': 8.6},
    {'title': 'The Dark Knight', 'category': 'Action', 'IMDB_score': 9.0},
    {'title': 'The Shawshank Redemption', 'category': 'Drama', 'IMDB_score': 9.3},
    {'title': 'The Matrix', 'category': 'Sci-Fi', 'IMDB_score': 8.7}
]

category = 'Sci-Fi'
print(f"Average IMDB score for {category} movies:", average_imdb_score_by_category(category, movies))