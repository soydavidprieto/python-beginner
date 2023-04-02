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

def search(source, source_name):
    if source == list(GENRES.keys()):
        print(f"Available: {source_name}(s): {source}")
        while True:
            ele1_list = []
            picker = input("Enter genre: ")
            for element in GENRES.items():
                if picker in element[0]:
                    ele1_list.append(element[1])
            if len(ele1_list):
                print(f"Available movies: {str(ele1_list[0])} with in {picker} genre")
                break
            else:
                print("Enter correct genre")
    elif source:
        print(f"Available: {source_name}(s): {source}")
        while True:
            ele2_list = []
            picker = input("Enter movie: ")
            for element in GENRES.items():
                if picker in element[1]:
                    ele2_list.append(element[0])
            if len(ele2_list):
                print(f"Movie to watch: '{picker}'. Genre(s): {str(ele2_list)}.")
                break
            else:
                print("Enter correct movie")
                continue

genre = search(source=list(GENRES.keys()), source_name="genres")
movie = search(source=GENRES['comedy'], source_name="movie")

# I not sure whether this is correct, maybe I didn't get the task properly, or there is some mistake in the description,
# but at least for now this function works as it should, but frankly saying I'm not satisfied with this solution, there should be something more smart:)