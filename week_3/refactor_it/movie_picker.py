def search(source, source_name='genre'):
    print(f'Available {source_name}(s): {source}')
    while True:
        value = input(f'Enter {source_name}:')
        if value in source:
            break
        else:
            print(f'{source_name} {value} not found. Please try again.')
            continue
    return value

def search_ext(source, source_name='genre', param_name='actor_name', param_type='actor' ):
    print(f'Available {source_name}(s): {source} with {param_name}')
    while True:
        value = input(f'Enter {source_name}:')
        if value in source:
            break
        else:
            print(f'{source_name} {value} with {param_type} {param_name} not found. Please try again.')
            continue
    return value

def search_movie(picked_actor):
    while True:
        entered_movie = input(' Enter movie: ')
        if entered_movie in actor_movies:
            break
        else:
            print('Movie ' + entered_movie + ' with actor ' + picked_actor + ' not found. Please try again.')
            continue
    return entered_movie

def search_actors():
    while True:
        picked_actor = input(' Enter actor: ')
        if picked_actor in allactors:
            break
        else:
            print('Actor ' + picked_actor + ' not found. Please try again.')
            continue
    return picked_actor

if __name__ == '__main__':
    print('Tasks 18. Movie picker 2.')

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
        picked_genre = search(source=list(genres.keys()), source_name='genre')
        entered_movie = search(source=genres[picked_genre], source_name='movie')
        print('Movie to watch: ' + entered_movie + '.' + ' Genre: ' + picked_genre + '.')
    elif search_genre == 'n':
        search_actor = input(' > Search by Actor: ')
        if search_actor == 'y':
            all_actors = set()
            for x in castkeys:
                for y in x:
                    all_actors.add(y)
            actor_movies = set()
            found_actor = search(source=list(all_actors), source_name='actor')
            for a in cast:
                for b in cast.get(a):
                    if b == found_actor:
                        actor_movies.add(a)

            found_movie = search_ext(actor_movies, 'movie', found_actor, 'actor')
            print('Movie to watch: ' + found_movie + '.' + ' Starring: ' + found_actor + '.')