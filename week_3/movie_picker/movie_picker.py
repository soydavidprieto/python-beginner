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

    search_by_genre = input('Search by Genre? y/n: ')

    if search_by_genre == 'y':
        print('Available Genres:', list(GENRES.keys()))
        genre = input('Enter genre: ')
        available_movies = {key: value for (key, value) in GENRES.items() if genre == key}
        print('Available Movies:', list(available_movies.values()))
        movie = input('Enter movie: ')
        print('Movie to watch:', movie, "Genre: ", genre)
    elif search_by_genre == 'n':
        search_by_actor = input('Search by Actor? y/n: ')
        print('Available Actors:', list(ACTORS.keys()))
        actor = input('Enter actor: ')
        available_movies = {key: value for (key, value) in ACTORS.items() if actor == key}
        print('Available Movies:', list(available_movies.values()))
        movie = input('Enter movie: ')
        print('Movie to watch:', movie, "Starring: ", actor)
    else:
        print("Something went wrong. Try again")

# this program doesn't cover the cases when user enters invalid data