if __name__ == '__main__':
    print('Tasks 15. Movie picker.')

    genre = {
        'comedy': ['Meet the Parents', 'Anger Management'],
        'adventures': 'Mommy',
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': 'Meet Joe Black',
        'thriller': 'Vanilla Sky',
        'action': 'Mission Impossible'
    }
    # TODO: [Mykyta] see task, actors are replaced with CAST
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

    genrekeys = list(genre.keys())
    actorkeys = list(actors.keys())

    search_genre = input(' > Search by Genre: ')
    if search_genre == 'y':
        print('Available Genres: ', genrekeys)
        while True:
            picked_genre = input(' Enter genre: ')
            if picked_genre in genrekeys:
                print('Available Movies:', genre.get(picked_genre))
                break
            else:
                print('Genre' + picked_genre + 'not found. Please try again.')
                continue
        while True:
            entered_movie = input(' Enter movie: ')
            if entered_movie in genre.get(picked_genre):
                print('Movie to watch: ' + entered_movie + '.' + ' Genre: ' + picked_genre + '.')
                break
            else:
                print('Movie ' + entered_movie + 'not found. Please try again.')
    elif search_genre == 'n':
        search_actor = input(' > Search by Actor: ')
        if search_actor == 'y':
            print('Available Actors: ', actorkeys)
            while True:
                picked_actor = input(' Enter actor: ')
                if picked_actor in actorkeys:
                    print('Available movies:', actors.get(picked_actor), 'with', picked_actor)
                    break
                else:
                    print('Actor ' + picked_actor + ' not found. Please try again.')
                    continue
            while True:
                entered_movie = input(' Enter movie: ')
                if entered_movie in actors.get(picked_actor):
                    print('Movie to watch: ' + entered_movie + '.' + ' Starring: ' + picked_actor + '.')
                    break
                else:
                    print('Movie ' + entered_movie + ' with actor ' + picked_actor + ' not found. Please try again.')
                    continue
