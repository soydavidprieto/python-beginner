# Task 15
Movie picker. Idea behind this task is to cover `if`, `while`, `for`. So there are 3 parts.
Before you start, pull the latest changes first:

In your branch `feat/<yourname>`.
```shell
# pull into your branch latest changes (commits) from `main`
git pull origin main
```

Our program picks a movie based on user's input. Consider `GENRES` and `ACTORS` as database tables (or key & value storage).
As a user, I want to search for a movie: 
1. based on `Genre`
2. based on `Actor`

```python
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
```

# Part 1. If statement.
Now, we start from a program which uses only `if` statement. 
This is a simple program, which should ends, when user's input is wrong. 
We are not covering repeats yet here.

Example of a program (search based on `Genre`).
```python
# Input: > Search by Genre: y
# Output: Available Genres: ['comedy', 'adventures', 'romantic', 'drama', 'thriller', 'action']
# Input: > Enter genre: comedy
# Output: Available Movies: ['Meet the Parents', 'Anger Management']
# Input: > Enter movie: Anger Management
# Output: Movie to watch: Anger Management. Genre: comedy.
```

Example of a program (search based on `Actor`).
```python
# Input: > Search by Genre: n
# Input: > Search by Actor: y
# Output: Available Actors: ['Robert De Niro', 'Ben Stiller', 'Adam Sandler', 'Jack Nicholson', 'Brendan Fraser', 'Rachel Weisz', 'Tom Cruise', 'Penelope Cruz', 'Cameron Diaz', 'Brad Pitt', 'Anthony Hopkins', 'Jeremy Renner']
# Input: > Enter actor: Tom Cruise
# Output: Available movies: ['Vanilla Sky', 'Mission Impossible'] with Tom Cruise
# Input: > Enter movie: Mission Impossible
# Output: Movie to watch: Mission Impossible. Starring: Tom Cruise.
```

## Commit your changes.
```shell
git add week_3/movie_picker/movie_picker.py
git commit -m "movie_picker (task 15)"
git push
```

# Part 2. For loop.
Now, business have changed the requirements, they don't support `ACTORS` table anymore, but there is another table called `CAST` now.
Business does not want users to see any changes (from console program perspective, everything should be the same). 
Rework your program in order to use `CAST` instead of `ACTORS`.
```python
GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}


# (!) ACTORS storage does not exist anymore.
# ACTORS = {
#     'Robert De Niro': ['Meet the Parents'],
#     'Ben Stiller': ['Meet the Parents'],
#     'Adam Sandler': ['Anger Management'],
#     'Jack Nicholson': ['Anger Management'],
#     'Brendan Fraser': ['Mummy'],
#     'Rachel Weisz': ['Mummy'],
#     'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
#     'Penelope Cruz': ['Vanilla Sky'],
#     'Cameron Diaz': ['Vanilla Sky'],
#     'Brad Pitt': ['Meet Joe Black'],
#     'Anthony Hopkins': ['Meet Joe Black'],
#     'Jeremy Renner': ['Mission Impossible']
# }


CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}
```

Example of a program (search based on `Genre`) (unchanged).
```python
# Input: > Search by Genre: y
# Output: Available Genres: ['comedy', 'adventures', 'romantic', 'drama', 'thriller', 'action']
# Input: > Enter genre: comedy
# Output: Available Movies: ['Meet the Parents', 'Anger Management']
# Input: > Enter movie: Anger Management
# Output: Movie to watch: Anger Management. Genre: comedy.
```

Example of a program (search based on `Actor`) (unchanged).
```python
# Input: > Search by Genre: n
# Input: > Search by Actor: y
# Output: Available Actors: ['Robert De Niro', 'Ben Stiller', 'Adam Sandler', 'Jack Nicholson', 'Brendan Fraser', 'Rachel Weisz', 'Tom Cruise', 'Penelope Cruz', 'Cameron Diaz', 'Brad Pitt', 'Anthony Hopkins', 'Jeremy Renner']
# Input: > Enter actor: Tom Cruise
# Output: Available movies: ['Vanilla Sky', 'Mission Impossible'] with Tom Cruise
# Input: > Enter movie: Mission Impossible
# Output: Movie to watch: Mission Impossible. Starring: Tom Cruise.
```

## Commit your changes.
```shell
git add week_3/movie_picker/movie_picker.py
git commit -m "movie_picker (task 16)"
git push
```

# Part 3. While loop.
Now, we want to NOT end our program, when user inputs wrong answers. 
We want to handle repeats now.

Example of a program (search based on `Genre`).
```python
# Input: > Search by Genre: y
# Output: Available Genres: ['comedy', 'adventures', 'romantic', 'drama', 'thriller', 'action']
# Input: > Enter genre: comed
# Output: Genre comed not found. Please try again.
# Input: > Enter genre: advent
# Output: Genre advent not found. Please try again.
# Input: > Enter genre: romantic
# Output: Available Movies: ['Vanilla Sky', 'Meet Joe Black']
# Input: > Enter movie: Vanilla Ski
# Output: Movie Vanilla Ski not found. Please try again.
# Input: > Enter movie: Vanilla Sky
# Output: Movie to watch: Vanilla Sky. Genre: romantic.
```

Example of a program (search based on `Actor`).
```python
# Input: > Search by Genre: n
# Input: > Search by Actor: y
# Output: Available Actors: ['Robert De Niro', 'Ben Stiller', 'Adam Sandler', 'Jack Nicholson', 'Brendan Fraser', 'Rachel Weisz', 'Tom Cruise', 'Penelope Cruz', 'Cameron Diaz', 'Brad Pitt', 'Anthony Hopkins', 'Jeremy Renner']
# Input: > Enter actor: Tom Cru
# Output: Actor Tom Cru not found. Please try again.
# Input: > Enter actor: Tom Cruis
# Output: Actor Tom Cruis not found. Please try again.
# Input: > Enter actor: Tom Cruise
# Output: Available movies: ['Vanilla Sky', 'Mission Impossible'] with Tom Cruise
# Input: > Enter movie: Mission Impossi
# Output: Movie Mission Impossi with actor Tom Cruise not found. Please try again.
# Input: > Enter movie: Mission Impossible
# Output: Movie to watch: Mission Impossible. Starring: Tom Cruise.
```

## Commit your changes.
```shell
git add week_3/movie_picker/movie_picker.py
git commit -m "movie_picker (task 17)"
git push
```
