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


search_type = input("Search by Genre: (y for yes, n for no) ")
if search_type == "y":
    print(f'Available Genres: {GENRES.keys()}')
    genre= input("Enter genre: ")
    if genre in GENRES.keys():
        print(f'Available Movies: {GENRES[genre]}')
        movie = input("Enter movie: ")
        if movie in GENRES[genre]:
            print(f"Movie to watch: {movie}. Genre: {genre}.")
        else:
            print("Wrong title.")
    else:
        print("Wrong genre!")

elif search_type == "n":
    search_actor = input("Search by Actors: (y for yes, n for no) ")
    if search_actor == "y":
        print(f'Available Actors: {ACTORS.keys()}')
        actor = input("Enter actor: ")
        if actor in ACTORS.keys():
            print(f'Available Movies: {ACTORS[actor]}')
            movie = input("Enter movie: ")
            if movie in ACTORS[actor]:
                print(f"Movie to watch: {movie}. Starring: {actor}.")
            else:
                print("Wrong title.")
        else:
            print("Wrong name!")

else:
    print("Wrong choice. Enter y for yes and n for no")
