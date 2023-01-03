if __name__ == '__main__':
    genres = {
        'comedy': ['Meet the Parents', 'Anger Management'],
        'adventures': ['Mummy'],
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': ['Meet Joe Black'],
        'thriller': ['Vanilla Sky'],
        'action': ['Mission Impossible']
    }

    actors = {
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

    search_by_genre = input('Search by Genre (y/n): ')
    if search_by_genre == 'y':
        print("Available Genres:", list(genres.keys()))
        genre_choice = input('Enter genre: ')
        for i in genres.keys():
            if i == genre_choice:
                print("Available Movies:", genres.get(i))
                available_movies = genres.get(i)
                movie_choice = input('Enter movie: ')
                if movie_choice in available_movies:
                    print('Movie to watch: {0}. Genre: {1}.'.format(movie_choice, genre_choice))
    elif search_by_genre == 'n':
        search_by_actor = input('Search by Actor (y/n): ')
        print("Available Actors:", list(actors.keys()))
        actor_choice = input('Enter actor: ')
        for i in actors.keys():
            if i == actor_choice:
                print('Available Movies: {0} with {1}'.format(actors.get(i), actor_choice))
                available_movies = actors.get(i)
                movie_choice = input('Enter movie: ')
                if movie_choice in available_movies:
                    print('Movie to watch: {0}. Starring: {1}.'.format(movie_choice, actor_choice))
