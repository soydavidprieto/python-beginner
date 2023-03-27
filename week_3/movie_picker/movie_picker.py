if __name__ == '__main__':
    print('Tasks 15-17. Movie picker.')

    GENRES = {
        'comedy': ['Meet the Parents', 'Anger Management'],
        'adventures': ['Mummy'],
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': ['Meet Joe Black'],
        'thriller': ['Vanilla Sky'],
        'action': ['Mission Impossible']
    }

    # (!) ACTORS storage does not exist anymore.
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

    CAST = {
        'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
        'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
        'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
        'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
        'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
        'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
    }
    available_actors = []

    search_by_genre = input('Search by Genre? y/n: ')
    if search_by_genre == 'y':
        print('Available Genres:', list(GENRES.keys()))
        while True:
            genre = input('Enter genre: ')
            if str(genre) in GENRES.keys():
                available_movies = {key: value for (key, value) in GENRES.items() if genre == key}
                break
            print("Genre ", genre, " not found. Please try again.")
        print('Available Movies:', list(available_movies.values()))
        while True:
            movie = input('Enter movie: ')
            if str(movie) in str(available_movies.values()):  # TODO: [Mykyta] if movie in available_movies.values()
                print('Movie to watch:', movie, "Genre: ", genre)
                break
            print("Movie ", movie, " not found. Please try again.")
    elif search_by_genre == 'n':
        search_by_actor = input('Search by Actor? y/n: ')
        for key, val in CAST.items():
            for i in val:
                available_actors.append(i)
        print('Available Actors:', available_actors)
        while True:
            actor = input('Enter actor: ')
            if str(actor) in str(available_actors):  # TODO: [Mykyta] if movie in available_movies.values()
                # TODO: [Mykyta] if actor in value
                available_movies = {key: value for (key, value) in CAST.items() if str(actor) in str(value)}
                print('Available Movies:', list(available_movies.keys()))
                break
            print("Actor ", actor, " not found. Please try again.")
        while True:
            movie = input('Enter movie: ')
            # TODO: [Mykyta] if movie in available_movies
            if str(movie) in str(available_movies.keys()):
                print('Movie to watch:', movie, "Starring: ", actor)
                break
            print("Movie ", movie, " not found. Please try again.")
    else:
        print("Something went wrong. Try again")