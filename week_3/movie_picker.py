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
CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}
# task 15
# film_picker = input("Search by Genre:  ")
# if film_picker == "y":
#     print(f"Available Genres:  {list(GENRES.keys())}")
#     genre_picker = input("Enter genre: ")
#     if genre_picker == "comedy":
#         print(f"Available Movies:  {GENRES['comedy']}")
#     movie_1 = input(f"Enter movie: ")
#     if movie_1 == "Anger Management":
#         print(f"Movie to watch: {GENRES['comedy'][1]}. Genre: {list(GENRES.keys())[0]}.")
#
# elif film_picker == "n":
#     actor = input("Search by Actor:  ")
#     if film_picker == "y":
#         print(f"Available Actors: {list(ACTORS.keys())}")
#     actor_name = input("Enter actor: ")
#     if actor_name == "Tom Cruise":
#         print(f"Available movies: {ACTORS['Tom Cruise']} with Tom Cruise")
#     movie_2 = input("Enter movie: ")
#     if movie_2 == "Mission Impossible":
#         print(f"Movie to watch: {ACTORS['Tom Cruise'][1]}. Starring: {list(ACTORS.keys())[6]} ")


# task 16
# list_films = []
# film_picker = input("Search by Genre:  ")
# if film_picker == "y":
#     print(f"Available Genres:  {list(GENRES.keys())}")
#     genre_picker = input("Enter genre: ")
#     if genre_picker == "comedy":
#         print(f"Available Movies:  {GENRES['comedy']}")
#     movie_1 = input(f"Enter movie: ")
#     if movie_1 == "Anger Management":
#         print(f"Movie to watch: {GENRES['comedy'][1]}. Genre: {list(GENRES.keys())[0]}.")
# elif film_picker == "n":
#     actor = input("Search by Actor:  ")
#     if film_picker == "y":
#         print(f"Available Actors: {list(CAST.keys())}")
#     actor_name = input("Enter actor: ")
#     for movie_to_watch, starring in CAST.items():
#         if actor_name in starring:
#             list_films.append(movie_to_watch)
#     print(f"Available movies: {list_films} with Tom Cruise")
#     film_by_actor = input("Enter movie: ")
#     if film_by_actor == "Mission Impossible":
#         print(f"Movie to watch: {list(CAST.keys())[5]}. Starring: {CAST['Mission Impossible'][0]}")

# task 17
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
    # TODO: [Mykyta] No names should be hardcoded, any movie can be picked from the list for any actor
    if input("Search fo actors? ") == 'y':
        while True:
            actor = input("Enter actor: ")
            movies_1 = []
            for value in CAST.items():
                if actor in value[1]:
                    movies_1.append(value[0])
            if len(movies_1):
                print(f"Available movies {movies_1} with {actor}")
            else:
                print(f"No actor named {actor} was found")
                continue
            break
            # TODO: [Mykyta] No names should be hardcoded, any movie can be picked from the list for any actor
        while True:
            movie = input("Enter movie: ")
            movies_2 = []
            for movie_name in CAST.items():
                if movie in movie_name[0]:
                    movies_2.append(movie_name[0])
            if len(movies_2):
                print(f"Movie to watch {movie} Starring {actor}")
            else:
                print(f"Movie: {movie} with actor {actor} not found. Please try again.")
                continue
            break


