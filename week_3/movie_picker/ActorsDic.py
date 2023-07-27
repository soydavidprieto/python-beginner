# (!) ACTORS storage does not exist anymore.
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

GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}


def search():
    print(ACTORS)
    searchActor = input('Insert an actor name: ')
    if searchActor in ACTORS:
        print(ACTORS[searchActor])
        searchMovieInput = input('Insert a movie title: ')
        movies = ACTORS[searchActor]
        if searchMovieInput in movies:
            print(searchMovieInput)
        else:
            print("Movie don´t exist for that actor")
    else:
        print('write a valid input')


def searchGenere():
    print(GENRES)
    searchGenere = input('Insert an actor name: ')
    if searchGenere in GENRES:
        print(GENRES[searchGenere])
        searchMovieGenere = input('Insert a movie title: ')
        movies = GENRES[searchGenere]
        if searchMovieGenere in GENRES:
            print(searchMovieGenere)
        else:
            print("Movie don´t exist for that actor")
    else:
        print('write a valid input')


search()
searchGenere()
