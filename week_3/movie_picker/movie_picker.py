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

list_1 = list(GENRES.keys())
list_2 = list(ACTORS.keys())


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
        a = input('Enter actor: ')
        if a not in ACTORS:
            print('Actors:', list_2)
        if a in list_2:
            print('Available movies: ', ACTORS.get(a))
        else:
            exit()
        m2 = input('Enter name of the movie: ')
        if m2 in ACTORS.get(a):
            print('Movie to watch:', m2 + '. ' 'Starring:', a)
        else:
            exit()
    if search_actor not in {'y', 'n'}:
        print('Please type "y" or "n" ')
    else:
        exit()

if search_genre not in {'y', 'n'}:
    print('Please type "y" or "n" ')
else:
    exit()


