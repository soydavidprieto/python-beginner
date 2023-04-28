if __name__ == '__main__':
    print('')

    genres = {
        'comedy': ['Meet the Parents', 'Anger Management'],
        'adventures': 'Mommy',
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': 'Meet JoeTasks 17. Movie picker. Black',
        'thriller': 'Vanilla Sky',
        'action': 'Mission Impossible'
    }

    cast = {
        'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
        'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
        'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
        'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
        'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
        'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
    }

    genrekeys = list(genres.keys())
    castkeys = list(cast.values())

    search_genre = input(' > Search by Genre: ')
    if search_genre == 'y':
        print('Available Genres: ', genrekeys)
        while True:
            picked_genre = input(' Enter genre: ')
            if picked_genre in genrekeys:
                print('Available Movies:', genres.get(picked_genre))
                break
            else:
                print('Genre ' + picked_genre + ' not found. Please try again.')
                continue
        while True:
            entered_movie = input(' Enter movie: ')
            if entered_movie in genres.get(picked_genre):
                print('Movie to watch: ' + entered_movie + '.' + ' Genre: ' + picked_genre + '.')
                break
            else:
                print('Movie ' + entered_movie + ' not found. Please try again.')

    elif search_genre == 'n':
        search_actor = input(' > Search by Actor: ')
        if search_actor == 'y':
            allactors = set()

            for x in castkeys:
                for y in x:
                    allactors.add(y)

            actor_movies = set()

            print('Available Actors: ', allactors)

            while True:
                picked_actor = input(' Enter actor: ')
                if picked_actor in allactors:
                    break
                else:
                    print('Actor ' + picked_actor + ' not found. Please try again.')
                    continue

            for a in cast:
                for b in cast.get(a):
                    if b == picked_actor:
                         actor_movies.add(a)


            print('Available movies:', actor_movies, 'with ', picked_actor)

            while True:
                    entered_movie = input(' Enter movie: ')
                    if entered_movie in actor_movies:
                        #print('Movie to watch: ' + entered_movie + '.' + ' Starring: ' + picked_actor + '.')
                        break
                    else:
                        print('Movie ' + entered_movie + ' with actor ' + picked_actor + ' not found. Please try again.')
                        continue
            print('Movie to watch: ' + entered_movie + '.' + ' Starring: ' + picked_actor + '.')
