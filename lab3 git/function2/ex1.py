def is_good_movie(movie):
    return movie['IMDB_score'] > 5.5
movie = {'title': 'Inception', 'IMDB_score': 8.8}
print(is_good_movie(movie)) 

