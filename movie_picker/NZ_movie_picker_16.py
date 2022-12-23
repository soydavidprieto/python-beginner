if __name__ == '__main__':
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

    by_genre = input("Search by genre: ").strip()
    if by_genre == 'y':
        print('Available genres:', list(GENRES.keys()))
        genre = input("Enter genre: ").strip()
        if genre in GENRES:
            films = GENRES[genre]
            print(f'Available Movies: {films}')
            film = input('Enter movie:')
            if film in films:
                print(f'Movie to watch: {film}, Genre: {genre}')
    else:
        by_actors = input("Search by Actors: ").strip()
        if by_actors == 'y':
            print('Available Actors:', list(ACTORS.keys()))
            actor = input('Enter actor: ').strip()
            if actor in ACTORS:
                movies = ACTORS[actor]
                print(f'Available movies: {movies} , with {actor}')
                movie = input("Enter movie: ").strip()
                if movie in movies:
                    print(f'Movie to watch: {movie},  Starring: {actor} ')
