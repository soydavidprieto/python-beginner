if __name__ == '__main__':

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
    
print('Available keys:')
for key in GENRES.keys():
    print(key)
inputgenre=input('Select Genre:' )

if inputgenre in GENRES:
    movies=GENRES[inputgenre]
    print('Movies:'+ str(GENRES[inputgenre]))
    userchoise=input('Select movie:')
    if userchoise in movies:
        print(userchoise + ", Genre:" + inputgenre)


print('Available actors:')
for key in ACTORS.keys():
    print(key)
inputactor=input('Select actor:')

if inputactor in ACTORS:
    films=ACTORS[inputactor]
    print('Films:' + str(ACTORS[inputactor]) + ' with ' + inputactor)
    userfilm=input('Select film:')
    if userfilm in films:
        print('Film to watch: ' + userfilm + ', Starring ' + inputactor)
    
