from iteration_utilities import deepflatten

GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}
CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

list_1 = list(GENRES.keys())
list_2 = list(deepflatten(list(CAST.values()), depth=1))

search_genre = input('Search by genre: ')
if search_genre == 'y':
    g = input('Enter genre: ')
    if g not in GENRES:
        print('Available genres:', list_1)
    if g in list_1:
        print('Available movies: ', GENRES.get(g))
    else:
        exit()
    m = input('Enter name of the movie: ')
    if m in GENRES.get(g):
        print('Movie to watch:', m + '. ' 'Genre:', g)
    else:
        exit()

elif search_genre == 'n':
    search_actor = input('Search by actor: ')
    if search_actor == 'y':
        print('Available actors: ', list_2)
        a = input('Enter actor: ')
        if a not in list_2:
            exit()

        starring = set()

        for i in CAST:
            for y in CAST.get(i):
                if y == a:
                    starring.add(i)
        print('Available movies: ', starring)

        m2 = input('Enter movie: ')
        if m2 in starring:
            print('Movie to watch:', m2 + '. ' 'Starring:', a)
    if search_actor not in {'y', 'n'}:
        print('Please type "y" or "n" ')

if search_genre not in {'y', 'n'}:
    print('Please type "y" or "n" ')
else:
    exit()
