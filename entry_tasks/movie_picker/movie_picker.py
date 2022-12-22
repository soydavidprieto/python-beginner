if __name__ == "__main__":
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

    def search_by_genre():
        all_genres = ", ".join(list(GENRES.keys()))
        print(f"{'Available Genres: '} {all_genres}")
        user_choose_gerne = input("Enter genre: ").strip()
        if user_choose_gerne in GENRES:
            movies_list = GENRES[user_choose_gerne]
            print(f'Available movies: {movies_list}')
            user_choose_film = input("Enter movie: ").strip()
            if user_choose_film in GENRES[user_choose_gerne]:
                print(f'Movie to watch: {user_choose_film}. Genre: {user_choose_gerne}.')
            else:
                print('Incorrect film name! Try again')
        else:
            print('Incorrect gerne! Try again')

    def search_by_actor():
        all_actors = ", ".join(list(ACTORS.keys()))
        print(f"{'Available Actors: '} {all_actors}")
        user_choose_actor = input("Enter actor: ").strip()
        if user_choose_actor in ACTORS:
            movies_list = ACTORS[user_choose_actor]
            print(f'Available movies: {movies_list}')
            user_choose_movie = input('Enter movie: ').strip()
            if user_choose_movie in ACTORS[user_choose_actor]:
                print(f'Movie to watch: {user_choose_movie}. Starring: {user_choose_actor}.')
            else:
                print('Incorrect movie name! Try again')
        else:
            print('Incorrect actor name! Try again')

    answer = input("Search by genre: ").strip()
    if answer == 'y':
        search_by_genre()
    elif answer == 'n':
        actor = input("Search by actor: ").strip()
        if actor == 'y':
            search_by_actor()
        elif answer == 'n':
            print('I really do not understand what you want!')
    else:
        print("Invalid input. Please enter 'y' or 'n'. Try again!")
