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

search_type = ''
while search_type != 'y' or 'n':  # TODO: [Mykyta] this is hard to read -> while search_type in {'y', 'n'}
    search_type = input('Search by genre (y or n): ')
    if search_type == "y":
        print(f'Available genres: {GENRES.keys()}')
        genre = input('Enter genre: ')
        while genre not in GENRES.keys(): # TODO: [Mykyta] -> while genre not in GENRES; `in` checks keys by default
            print(f'Genre {genre} not found. Please try again.')
            genre = input('Enter genre: ')
        print(f'Avalaible movies: {GENRES[genre]}')
        movie = input('Enter movie: ')
        while movie not in GENRES[genre]:
            print(f'Movie {movie} not found. Please try again.')
            movie = input('Enter movie: ')
        print(f'Movie to watch: {movie}. Genre: {genre}.')

    elif search_type == "n":
        search_actor = ''
        while search_actor != 'y' or 'n':
            search_actor = input('Search by actor (y or n): ')
            if search_actor == "y":
                actors_list = []
                for actors in CAST.values():
                    actors_list += actors
                    unique_actors = set(actors_list)
                print(f'Available Actors: {unique_actors}')
                actor = input('Enter actor: ')
                while actor not in unique_actors:
                    print(f'Actor {actor} not found. Please try again.')
                    actor = input('Enter actor: ')
                movies_list = []
                for value in CAST.values():
                    if actor in value:
                        keys = [k for k, v in CAST.items() if v == value]
                        movies_list += keys
                print(f'Avalaible movies: {movies_list}')
                movie = input('Enter movie: ')
                while movie not in movies_list:
                    print(f'Movie {movie} with actor {actor} not found. Please try again.')
                    movie = input('Enter movie: ')
                print(f'Movie to watch: {movie}. Starring: {actor}.')
                break
            else:
                print("OK, good bye!")
                break
    break
