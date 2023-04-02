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

while True:
    search_genre = input('Search by genre: ')
    if search_genre == 'y':
        print('Available genres:', list_1)
        while True:
            g = input('Enter genre: ')
            if g in list_1:
                print('Available movies: ', GENRES.get(g))
                break
            else:
                print('Genre', g, 'not found. Please try again.')

        while True:
            m = input('Enter name of the movie: ')
            if m in GENRES.get(g):
                print('Movie to watch:', m + '. ' 'Genre:', g)
                break
            else:
                print('Movie', m, 'not found. Please try again.')
        break

    if search_genre == 'n':
        while True:
            search_actor = input('Search by actor: ')
            if search_actor == 'y':
                print('Available actors: ', list_2)
                while True:
                    a = input('Enter actor: ')
                    if a in list_2:
                        break
                    else:
                        print('Actor', a, 'not found. Please try again.')

                starring = set()

                for i in CAST:
                    for y in CAST.get(i):
                        if y == a:
                            starring.add(i)
                print('Available movies: ', starring)

                while True:
                    m2 = input('Enter movie: ')
                    if m2 in starring:
                        print('Movie to watch:', m2 + '. ' 'Starring:', a)
                        break
                    else:
                        print('Movie', m2, 'not found. Please try again.'),
                break
            if search_actor == 'n':
                print('Goodbye!')
                exit()
            else:
                print('Please type "y" or "n" ')
        exit()
    else:
        print('Please type "y" or "n" ')


