GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}


ACTORS = {
    'Robert De Niro': ['Meet the Parents'],
    'Ben Stiller': ['Meet the Parents'],
    'Adam Sandler': ['Anger Management'],
    'Jack Nicholson': ['Anger Management'],
    'Brendan Fraser': ['Mummy'],
    'Rachel Weisz': ['Mummy'],
    'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
    'Penelope Cruz': ['Vanilla Sky'],
    'Cameron Diaz': ['Vanilla Sky'],
    'Brad Pitt': ['Meet Joe Black'],
    'Anthony Hopkins': ['Meet Joe Black'],
    'Jeremy Renner': ['Mission Impossible']
}

CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

search_type = input('Search by genre (y or n): ')
if search_type == "y":
    print(f'Available genres: {GENRES.keys()}')
    genre = input('Enter genre: ')
    if genre in GENRES.keys():
        print(f'Avalaible movies: {GENRES[genre]}')
        movie = input('Enter movie: ')
        if movie in GENRES[genre]:
            print(f'Movie to watch: {movie}. Genre: {genre}.')
        else:
            print("Wrong title")
    else:
        print("Wrong genre!")

elif search_type == "n":
    search_actor = input('Search by actor (y or n): ')
    if search_actor == "y":
        actors_list = []
        for actors in CAST.values():
            actors_list += actors
            unique_actors = set(actors_list)
        print(f'Available Actors: {unique_actors}')
        actor = input('Enter actor: ')
        if actor in unique_actors:
            movies_list = []
            for value in CAST.values():
                if actor in value:
                    keys = [k for k, v in CAST.items() if v == value]
                    movies_list += keys
            print(f'Avalaible movies: {movies_list}')
            movie = input('Enter movie: ')
            if movie in movies_list:
                print(f'Movie to watch: {movie}. Starring: {actor}.')
            else:
                print("Wrong title")
        else:
            print("Wrong name!")
else:
    print('You were supposed to choose between "y" and "n". Good bye!')



