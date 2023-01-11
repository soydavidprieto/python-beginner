def search(data, key, source=None):
    films = data[key]
    print(f'Available Movies: {films}')
    film = input('Enter movie:')
    if film in films:
        print(f'Movie to watch: {film}, {source}: {key}')
    return film


if __name__ == '__main__':
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

    by_genre = input("Search by genre: ").strip()
    if by_genre == 'y':
        print('Available genres:', list(GENRES.keys()))
        genre = input("Enter genre: ").strip()
        if genre in GENRES:
            film = search(data=GENRES, key=genre, source="Genre")
            # films = GENRES[genre]
            # print(f'Available Movies: {films}')
            # film = input('Enter movie:')
            # if film in films:
            #     print(f'Movie to watch: {film}, Genre: {genre}')

    else:
        by_cast = input("Search by cast:").strip()
        if by_cast == 'y':
            ACTORS = dict()
            for film, actors in CAST.items():
                for actor in actors:
                    if actor in ACTORS:
                        ACTORS[actor].append(film)
                    else:
                        ACTORS[actor] = [film]
            print('Available actors:', list(ACTORS.keys()))
            actor = input('Enter Actor:').strip()
            if actor in ACTORS:
                search(ACTORS, actor, source="Actor")
                # movies = ACTORS[actor]
                # print(f'Movie to watch:{movies}, with actor {actor}')

# ACTORS = dict()
# for film, actors in CAST.items():
#     for actor in actors:
#         if actor in ACTORS:
#             ACTORS[actor].append(film)
#         else:
#             ACTORS[actor] = [film]
# print(ACTORS)
