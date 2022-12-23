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


    def search_by_genre_or_actor(search_type):
        if search_type == "genre":
            all_items = ", ".join(list(GENRES.keys()))
            item_type = "genre"
            items_dict = GENRES
        elif search_type == "actor":
            all_items = ", ".join(list(ACTORS.keys()))
            item_type = "actor"
            items_dict = ACTORS
        else:
            print("Incorrect search type. Please enter either 'genre' or 'actor'.")
            return

        print(f"{'Available '}{item_type.capitalize()}s: {all_items}")
        user_choose_item = input(f"Enter {item_type}: ").strip()
        if user_choose_item in items_dict:
            movies_list = items_dict[user_choose_item]
            print(f'Available movies: {movies_list}')
            user_choose_movie = input('Enter movie: ').strip()
            if user_choose_movie in items_dict[user_choose_item]:
                print(
                    f'Movie to watch: {user_choose_movie}. Starring: {user_choose_item}.' if search_type == "actor" else
                    f'Movie to watch: {user_choose_movie}. Genre: {user_choose_item}.')
            else:
                print('Incorrect movie name! Try again')
        else:
            print(f'Incorrect {item_type} name! Try again')


    answer = input("Search by genre: ").strip()
    if answer == 'y':
        search_by_genre_or_actor('genre')
    elif answer == 'n':
        actor = input("Search by actor: ").strip()
        if actor == 'y':
            search_by_genre_or_actor('actor')
        elif answer == 'n':
            print('I really do not understand what you want!')
    else:
        print("Invalid input. Please enter 'y' or 'n'. Try again!")
