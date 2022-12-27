if __name__ == '__main__':

    GENRES = {
        'comedy': ['Meet the Parents', 'Anger Management'],
        'adventures': ['Mummy'],
        'romantic': ['Vanilla Sky', 'Meet Joe Black'],
        'drama': ['Meet Joe Black'],
        'thriller': ['Vanilla Sky'],
        'action': ['Mission Impossible']
    }

    CAST = {
        'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
        'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
        'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
        'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
        'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
        'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
    }


    def search(all_items, search_type):
        print(f"{'Available '}{search_type}s: {all_items}")
        user_choose_item = input(f"Enter {search_type}: ").strip()
        while user_choose_item not in all_items:
            user_choose_item = input(f"Enter {search_type}: ").strip()
        else:
            return user_choose_item


    def movies_by_actors(cast):
        inverted_dict = {}
        for movie, actors in cast.items():
            for actor in actors:
                inverted_dict[actor] = inverted_dict.get(actor, []) + [movie]
        return inverted_dict


    by_genre = input('Search by Genre: ').lower() == 'y'

    if by_genre:
        genre = search(all_items=list(GENRES.keys()), search_type='genre')
        movie = search(all_items=GENRES[genre], search_type='movie')
        print(f'Movie to watch: {movie}. Genre: {genre}.')
        exit()

    by_actor = input('Search by Actor: ').lower() == 'y'

    if by_actor:
        actors = movies_by_actors(CAST)
        actor = search(all_items=list(actors.keys()), search_type='actor')
        movie = search(all_items=actors[actor], search_type='movie')
        print(f'Movie to watch: {movie}. Starring: {actor}.')
        exit()

    print('Search available by Genre or Actor only. Please try again.')
