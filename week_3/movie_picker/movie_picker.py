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


    # ACTORS = {
    #     'Robert De Niro': ['Meet the Parents'],
    #     'Ben Stiller': ['Meet the Parents'],
    #     'Adam Sandler': ['Anger Management'],
    #     'Jack Nicholson': ['Anger Management'],
    #     'Brendan Fraser': ['Mummy'],
    #     'Rachel Weisz': ['Mummy'],
    #     'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
    #     'Penelope Cruz': ['Vanilla Sky'],
    #     'Cameron Diaz': ['Vanilla Sky'],
    #     'Brad Pitt': ['Meet Joe Black'],
    #     'Anthony Hopkins': ['Meet Joe Black'],
    #     'Jeremy Renner': ['Mission Impossible']
    # }

    CAST = {
        'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
        'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
        'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
        'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
        'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
        'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
    }
    genre_list = list(GENRES.keys())
    # actor_list = list(ACTORS.keys())


    bygenre = input('Search by Genre: ')
    # Genre
    if bygenre == 'y':
        print('Available Genres: ' + str(genre_list))
        while True:
            input_genre = input('Enter Genre: ')
            if input_genre in GENRES:
                print('Available Movies: ' + str(GENRES[input_genre]));
                break
            else:
                print(f'Genre {input_genre} not found. Please try again')
        while True:
            input_movie = input('Enter movie: ')
            if input_movie in GENRES[input_genre]:
                print('Movie to watch: ' + input_movie + ' Genre: ' + input_genre);
                break
            else:
                print(f'Movie {input_movie} not found. Please try again')

    # Actor
    elif bygenre == 'n':
        byactor = input('Search by Actor: ')
        if byactor == 'y':
            # print('Available Actors: ' + str(actor_list))
            # input_actor = input('Enter Actor: ')
            # print('Available Movies: ' + str(ACTORS[input_actor]))
            # input_movie = input('Enter movie: ')
            # print('Movie to watch: ' + input_movie + ' Starring: ' + input_actor)
            allactors = []
            # TODO: [Mykyta] Read: https://realpython.com/iterate-through-dictionary-python/#iterating-through-keys-directly
            for movie in CAST.keys():
                for actor in CAST[movie]:
                    allactors.append(actor)

            uniq_actors = list(set(allactors))
            print('Available Actors: ' + str(uniq_actors))

            while True:
                input_actor = input('Enter Actor: ')
                movies = []
                for movie in CAST.keys():
                    if input_actor in CAST[movie]:
                        movies.append(movie)
                if movies:
                    print('Available Movies: ' + str(movies))
                    break
                else:
                    print(f'Actor {input_actor} not found. Please try again.')

            while True:
                input_movie = input('Enter movie: ')
                if input_movie in movies:
                    print('Movie to watch: ' + input_movie + ' Starring: ' + input_actor)
                    break
                else:
                    print(f'Movie {input_movie} with actor {input_actor} not found. Please try again.')