if __name__ == '__main__':
    print('Tasks 16. Movie picker.')

genres = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
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
    picked_genre = input(' Enter genre: ')
    if picked_genre in genrekeys:
        print('Available Movies:', genre.get(picked_genre))
    else:
        exit()
    entered_movie = input(' Enter movie: ')
    if entered_movie in genre.get(picked_genre):
        print('Movie to watch: ' + entered_movie + '.' + ' Genre: ' + picked_genre + '.')
    else:
        exit()
elif search_genre == 'n':
    search_actor = input(' > Search by Actor: ')
    if search_actor == 'y':
        allactors = set()
        for x in castkeys:
            for y in x:
                allactors.add(y)
        print('Available Actors: ', allactors)
        picked_actor = input(' Enter actor: ')
        if picked_actor not in allactors:
            exit()

        actor_movies = set()

        for a in cast:
            for b in cast.get(a):
                if b == picked_actor:
                    actor_movies.add(a)
        print('Actor movies:', actor_movies)

        entered_movie = input(' Enter movie: ')
        if entered_movie in actor_movies:
            print('Movie to watch: ' + entered_movie + '.' + ' Starring: ' + picked_actor + '.')
        else:
            exit()

