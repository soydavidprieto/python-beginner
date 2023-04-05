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


def search(source, source_name):
    print(f'Available {source_name}(s): {source}')
    search_phrase = input(f'Enter {source_name}:')
    while search_phrase not in source:
        print(f'{source_name} not found. Please Try again.')
        search_phrase = input(f'Enter {source_name}:')
    return search_phrase


def movies_by_actors(cast):
    actors = {}
    actors_list = []
    for actor in CAST.values():
        actors_list += actor
    for actor in actors_list:
        movies_list = []
        for value in CAST.values():
            if actor in value:
                keys = [k for k, v in CAST.items() if v == value]
                movies_list += keys
        actors[actor] = movies_list
    return actors


search_type = input('Search by genre (yes or no): ')
while search_type not in {'yes', 'no'}:
    print('Wrong answer!')
    search_type = input('Do you want to search by genre? (yes or no): ')
if search_type == "yes":
    genre = search(source=list(GENRES.keys()), source_name='genre')
    movie = search(source=GENRES[genre], source_name='movie')
    print(f'Movie to watch: {movie}. Genre: {genre}.')

elif search_type == "no":
    search_actor = input('Search by actor (yes or no): ')
    while search_actor not in {'yes', 'no'}:
        print('Wrong answer!')
        search_actor = input('Search by actor (yes or no): ')
    if search_actor == "yes":
        actors = movies_by_actors(CAST)
        actor = search(source=list(actors.keys()), source_name='actor')
        movie = search(source=actors[actor], source_name='movie')
        print(f'Movie to watch: {movie}. Starring: {actor}.')
    else:
        print("OK, good bye!")

