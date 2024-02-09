def get_movies_by_category(category, movies):
    movies_in_category = [movie for movie in movies if movie['category'] == category]
    return movies_in_category

movies = [
    {'title': 'Inception', 'category': 'Sci-Fi'},
    {'title': 'Interstellar', 'category': 'Sci-Fi'},
    {'title': 'The Dark Knight', 'category': 'Action'},
    {'title': 'The Shawshank Redemption', 'category': 'Drama'},
    {'title': 'The Matrix', 'category': 'Sci-Fi'}
]

category = 'Sci-Fi'
movies_in_category = get_movies_by_category(category, movies)
print(f"Movies in the category '{category}':")
for movie in movies_in_category:
    print(movie['title'])