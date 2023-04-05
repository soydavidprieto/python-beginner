from collections import defaultdict

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
PG = {
    13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
    16: {'Vanilla Sky'}
}


# def search(source, source_name):
#     print(f"Available: {source_name}(s): {source}")
#     while True:
#         source_item = input(f"Enter {source_name}: ")
#         if source_item in source:
#             return source_item
#         print("Not found try again")
#
# genre = search(source=list(GENRES.keys()), source_name="genres")
# movie = search(source=GENRES[genre], source_name="movie")
# print(f"Watch {movie}  and genre is {genre}")
#
# def movies_by_actors(cast):
#     actors = {}
#     for key, value in cast.items():
#         for actor_name in value:
#             films = []
#             for key_value in cast.items():
#                 if actor_name in key_value[1]:
#                     films.append(key_value[0])
#                     actors.update({actor_name: films})
#     return actors
#
#
# # Usage example (search by actor):
# actors = movies_by_actors(CAST)
# actor = search(source=list(actors.keys()), source_name='actor')
# movie = search(source=actors[actor], source_name='movie')

def prepare(genres, pg_rate):
    new_genres = {}
    while True:
        try:
            age = input("Enter your age: ")
            age = int(age)
            if isinstance(age, int):
                break
        except ValueError:
            print("You have entered not digit symbol")
    if age in range(14):
        try:
            films = pg_rate[13]
        except KeyError:
            print("The Value is incorrect")
        for key, value in genres.items():
            for item in value:
                if item in films:
                    if key in new_genres:
                        string = new_genres[key]
                        string += "," + item
                        new_genres.update({key: string})
                    else:
                        new_genres.update({key: item})
    else:
        try:
            films = pg_rate[16]
        except KeyError:
            print("The Value is incorrect")
        for key, value in genres.items():
            for item in value:
                if item in films:
                    if key in new_genres:
                        string = new_genres[key]
                        string += "," + item
                        new_genres.update({key: string})
                    else:
                        new_genres.update({key: item})
    print(new_genres)
    return new_genres


prepare(genres=GENRES, pg_rate=PG)
