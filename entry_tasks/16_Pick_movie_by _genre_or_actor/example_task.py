GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}


# ACTORS = {
#     'Robert De Niro': ['Meet the Parents'],
#     'Ben Stiller': ['Meet the Parents'],
#     'Adam Sandler': ['Anger Management'],
#     'Jack Nicholson': ['Anger Management'],
#     'Brendan Fraser': ['Mummy'],
#     'Rachel Weisz': ['Mummy'],
#     'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
#     'Penelope Cruz': ['Vanilla Sky'],
#     'Cameron Diaz': ['Vanilla Sky'],
#     'Brad Pitt': ['Meet Joe Black'],
#     'Anthony Hopkins': ['Meet Joe Black'],
#     'Jeremy Renner': ['Mission Impossible']
# }

def movies_by_actors(cast):
    actors_with_movies = {}
    for movie_name in cast:
        for actor_name in cast[movie_name]:
            if actor_name not in actors_with_movies:
                actors_with_movies[actor_name] = [movie_name]
            else:
                actors_with_movies[actor_name].append(movie_name)
    return actors_with_movies


def search(source, source_name):
    print(f'Available {source_name}s: {source}')
    while True:
        input_name = input(f"Enter specific {source_name}: ").strip()
        if input_name in source:
            return input_name
        print(f"You've entered wrong {source_name} name. Please enter correct one.")


if __name__ == '__main__':
    by_genre = input('Search by Genre: ').lower() == 'y'
    if by_genre:
        genre = search(source=list(GENRES.keys()), source_name='genre')
        movie = search(source=GENRES[genre], source_name='movie')
        print(f'Movie to watch: {movie}. Genre: {genre}.')
        exit()

    by_actor = input('Search by Actor: ').lower() == 'y'

    if by_actor:
        actors = movies_by_actors(CAST)
        actor = search(source=list(actors.keys()), source_name='actor')
        movie = search(source=actors[actor], source_name='movie')
        print(f'Movie to watch: {movie}. Starring: {actor}.')
        exit()

    print('Search available by Genre or Actor only. Please try again.')
