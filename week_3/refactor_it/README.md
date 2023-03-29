# Task 18

## Part 1
Refactor `movie_picker.py` in order to minimize code duplication.
For example, manipulations with genres or cast look ups could be extracted to single function called `search`:
```python
def search(source, source_name='genre'):
    print(f'Available {source_name}(s): {source}')
    # should ask for an input and repeat unless match is found
    ...

# Usage example (search by genre):
# genre = search(source=list(GENRES.keys()), source_name='genre')
# movie = search(source=GENRES[genre], source_name='movie')
```

What about search by movie? `CAST` is not suited for `search` function. 
Remember, we replaced `ACTORS` by `CAST` in the beginning?
One option would be to recreate `ACTORS` from `CAST` back and use it as an input for the `search` function.

```python
def movies_by_actors(cast):
    actors = {}
    ...
    return actors

# Usage example (search by actor):
# actors = movies_by_actors(CAST)
# actor = search(source=list(actors.keys()), source_name='actor')
# movie = search(source=actors[actor], source_name='movie')
```

## Part 2
Also let's add minor modification to our movie picker.
We want to hide/show movies based on user's age. 
If it's greater that PG rate, we show it in the list, otherwise, filter it out.

```python
PG = {
    13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
    16: {'Vanilla Sky'}
}
```
1. Ask user about his age. (Make sure user provides an integer, `isinstance(value, int) is True`)
2. Pre-filter `GENRES` and `ACTORS` before processing based on `PG` (in order to not rework entire program). 
   User's age should be >= PG rate in order to watch the movie.

```python
def prepare(genres, pg_rate):
    new_genres = {}
    ...
    return new_genres
```
