GENRES = {
    "comedy": ["Meet the Parents", "Anger Management"],
    "adventures": ["Mummy"],
    "romantic": ["Vanilla Sky", "Meet Joe Black"],
    "drama": ["Meet Joe Black"],
    "thriller": ["Vanilla Sky"],
    "action": ["Mission Impossible"],
}
CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

cast_values = sum(CAST.values(), [])
unique_cast_values = list({value: "" for value in cast_values})
genres_values = sum(GENRES.values(), [])
lowercase_list = [str(x.lower()) for x in genres_values]
movie_dict = {lowercase_list[i]: genres_values[i] for i in range(len(lowercase_list))}


if __name__ == "__main__":
    input_values = ['y', 'n']
    is_search_by_genre = None
    while True:
        is_search_by_genre = input("Search by genre: ").strip()
        if is_search_by_genre == 'y':
            genres_keys = list(GENRES.keys())
            print(f'{">>> Available Genres: "} {genres_keys}')
            while True:
                genre = input("Enter specific genre: ").strip()
                if genre in genres_keys:
                    break
                print("You've entered wrong genre name. Please enter correct one.")
            movies = GENRES[genre]
            print(f'>>> Available movies: {movies}')
            while True:
                movie = input("Enter movie: ").strip()
                if movie.lower() in movie_dict.keys():
                    movies = movie_dict[movie.lower()]
                    print(f' >>> Movie to watch: {movies}. Genre: {genre}.')
                    break
                print("You've entered wrong movie name. Please enter correct one.")
            break

        elif is_search_by_genre == "n":
            input_values = ['y', 'n']
            is_search_by_cast = None
            while True:
                cast = input("Search by cast: ").strip()
                if cast == "y":
                    print(f'{">>> Available Actors: "} {cast_values}')
                    while True:
                        actor = input("Enter specific actor: ").strip()
                        if actor.title() in cast_values:
                            break
                        print("You've entered wrong actor name. Please enter correct one.")
                    list_of_movies = [key
                                      for key, list_of_values in CAST.items()
                                      if actor.title() in list_of_values]
                    if list_of_movies:
                        print(f'>>> Available movies: {list_of_movies} with {actor.title()}.')
                    while True:
                        movie = input("Enter movie: ").strip()
                        if movie.lower() in movie_dict.keys():
                            movies = movie_dict[movie.lower()]
                            print(f' >>> Movie to watch: {movies}. Starring: {actor.title()}.')
                            break
                        print("You've entered wrong movie name. Please enter correct one.")
                    break
                if cast == "n":
                    print("Searching completed.")
                    break
                else:
                    print("Enter 'y' or 'n' for searching by cast!")
            break
        else:
            print("Enter 'y or 'n' for searching by genre!")
