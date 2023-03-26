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
    genre_list = list(GENRES.keys())
    actor_list = list(ACTORS.keys())

    bygenre = input('Search by Genre: ')
    # Genre
    if bygenre == 'y':
        print('Available Genres: ' + str(genre_list))
        input_genre = input('Enter Genre: ')
        print('Available Movies: ' + str(GENRES[input_genre]));
        input_movie = input('Enter movie: ')
        print('Movie to watch: ' + input_movie + ' Genre: ' + input_genre);

    # Actor
    elif bygenre == 'n':
        byactor = input('Search by Actor: ')
        if byactor == 'y':
            print('Available Actors: ' + str(actor_list))
            input_actor = input('Enter Actor: ')
            print('Available Movies: ' + str(ACTORS[input_actor]));
            input_movie = input('Enter movie: ')
            print('Movie to watch: ' + input_movie + ' Starring: ' + input_actor);
