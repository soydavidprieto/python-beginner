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


def search(source, source_name):
    print(f"Available: {source_name}(s): {source}")
    while True:
        source_item = input(f"Enter {source_name}: ")
        if source_item in source:
            return source_item
        print("Not found try again")

genre = search(source=list(GENRES.keys()), source_name="genres")
movie = search(source=GENRES[genre], source_name="movie")
print(f"Watch {movie}  and genre is {genre}")

def movies_by_actors(cast):
    actors = {}
    for movie, actors_list in cast.items():
        for actor_name in actors_list:
            if actor_name in actors:
                actors[actor_name].append(movie)
            else:
                actors[actor_name] = [movie]
    print(actors)
    return actors


#Usage example (search by actor):
actors = movies_by_actors(CAST)
actor = search(source=list(actors.keys()), source_name='actor')
movie = search(source=actors[actor], source_name='movie')

def prepare(genres, pg_rate):
    new_genres = {}
    while True:
        try:
            age = input("Enter your age: ")
            age = int(age)
            break
        except ValueError:
            print("You have entered not digit symbol")
    for key_name in pg_rate:
        if age >= key_name:
            for film in pg_rate[key_name]:
                for key, value in genres.items():
                    for movie in value:
                        if film == movie:
                            if key in new_genres:
                                new_genres[key].append(movie)
                            else:
                                new_genres[key] = [movie]
    print(new_genres)
    return new_genres
prepare(genres=GENRES, pg_rate=PG)
