if __name__ == '__main__':
    print('Tasks 18. Movie picker 2.')


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

    PG = {
        13: ['Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'],
        16: ['Vanilla Sky']
    }

    def search_genre(genre, pg_rate):
        new_genres = {}
        if genre in GENRES.keys():
            genres = {key: value for (key, value) in GENRES.items() if genre == key}
            if int(pg_rate) >= 13:
                genres2 = {key: value for (key, value) in PG.items() if key == 13}
                new_genres = {key: value for (key, value) in genres.items() if genres.values() != genres2.values()}
                return new_genres
            elif int(pg_rate) >= 16:
                genres2 = {key: value for (key, value) in PG.items() if key == 16}
                new_genres = {key: value for (key, value) in genres.items() if genres.values() != genres2.values()}
                return new_genres
        else:
            print("Genre ", genre, " not found. Please try again.")


    def search_movie(movie, available_movies, source_name):
        if movie in str(available_movies):
            if source_name == 'genre':
                print('Movie to watch:', movie, "Genre: ", genre)
            elif source_name == 'actor':
                print('Movie to watch:', movie, "Starring: ", actor)
        else:
            print("Movie ", movie, " not found. Please try again.")


    def search_actor(actor, available_actors):
        if actor in str(available_actors):
            return {key: value for (key, value) in CAST.items() if str(actor) in str(value)}
        else:
            print("Actor ", actor, " not found. Please try again.")

    available_actors = []

    search_by_genre = input('Search by Genre? y/n: ')
    if search_by_genre == 'y':
        print('Available Genres:', list(GENRES.keys()))
        genre = input('Enter genre: ')
        age = input('Enter your age: ')
        print('Available Movies:', list(search_genre(genre, age).values()))
        movie = input('Enter movie: ')
        search_movie(movie, search_genre(genre, age).values(), 'genre')
    elif search_by_genre == 'n':
        search_by_actor = input('Search by Actor? y/n: ')
        for key, val in CAST.items():
            for i in val:
                available_actors.append(i)
        print('Available Actors:', available_actors)
        actor = input('Enter actor: ')
        print('Available Movies:', list(search_actor(actor,available_actors).keys()))
        movie = input('Enter movie: ')
        search_movie(movie, search_actor(actor,available_actors).keys(), 'actor')
    else:
        print("Something went wrong. Try again")

#Unfortunatly negative scenarios doesn't work. Need to cover cases when the user enter invalid data
#filter by age doesn't work yet