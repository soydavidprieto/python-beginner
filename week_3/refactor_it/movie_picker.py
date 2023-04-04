if __name__ == '__main__':
    print('Tasks 15-17. Movie picker.')

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

    def search(source, source_name='genre'):
        print(f'Available {source_name}(s): {source}')
        while True:
            user_input = input(f'Enter {source_name}: ')
            if user_input in source:
                break
            else:
                print(f'Genre {user_input} not found. Please try again')
        return user_input

    def movies_by_actors(cast):
        actors = {}
        for movie in cast.keys():
            for actor in cast[movie]:
                actors[actor] = movie
        return actors

    bygenre = input('Search by Genre: ')
    # Genre
    if bygenre == 'y':
        genre = search(source=list(GENRES.keys()), source_name='genre')
        movie = search(source=GENRES[genre], source_name='movie')
        print(f'Movie to watch: {movie} Genre: {genre}')

    # Actor
    elif bygenre == 'n':
        byactor = input('Search by Actor: ')
        if byactor == 'y':

            actors = movies_by_actors(CAST)
            actor = search(source=list(actors.keys()), source_name='actor')
            movie = search(source=actors[actor], source_name='movie')
            print(f'Movie to watch: {movie} Starring: {actor}')

