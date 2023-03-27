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
#task 15
film_picker = input("Search by Genre:  ")
if film_picker == "y":
    print(f"Available Genres:  {list(GENRES.keys())}")
    genre_picker = input("Enter genre: ")
    if genre_picker == "comedy":
        print(f"Available Movies:  {GENRES['comedy']}")
    movie_1 = input(f"Enter movie: ")
    if movie_1 == "Anger Management":
        print(f"Movie to watch: {GENRES['comedy'][1]}. Genre: {list(GENRES.keys())[0]}.")

elif film_picker == "n":
    actor = input("Search by Actor:  ")
    if film_picker == "y":
        print(f"Available Actors: {list(ACTORS.keys())}")
    actor_name = input("Enter actor: ")
    if actor_name == "Tom Cruise":
        print(f"Available movies: {ACTORS['Tom Cruise']} with Tom Cruise")
    movie_2 = input("Enter movie: ")
    if movie_2 == "Mission Impossible":
        print(f"Movie to watch: {ACTORS['Tom Cruise'][1]}. Starring: {list(ACTORS.keys())[6]} ")



