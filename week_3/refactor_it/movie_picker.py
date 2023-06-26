

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
searchGender = input('Insert a genere: ')

if searchGender == 'comedy' :
    print(GENRES['comedy'])

elif searchGender== 'adventures':
    print(GENRES['adventures'])
    
elif searchGender == 'romantic':
    print(GENRES['romantic'])

elif searchGender == 'drama' :
    print(GENRES['drama'])

elif searchGender == 'thriller' :
    print(GENRES['thriller'])
    
elif searchGender == 'action' :
    print(GENRES['action'])

else :
    print('The genere is not valid', (GENRES))
    

#Actor
ACTORSAcces = list(ACTORS)

searchActor = input('Insert an actor name: ')

if searchActor == 'Robert De Niro' :
    print(ACTORS['Robert De Niro'])
    
elif searchActor == 'Ben Stiller' :
    print(ACTORS['Ben Stiller'])

elif searchActor == 'Adam Sandler':
    print(ACTORS['Adam Sandler'])
    
elif searchActor == 'Jack Nicholson' :
    print(ACTORS['Jack Nicholson'])
    
elif searchActor == 'Brendan Fraser' :
    print([ACTORS['Brendan Fraser']])

elif searchActor == 'Rachel Weisz':
    print(ACTORS['Rachel Weisz'])
    
elif searchActor == 'om Cruise' :
    print(ACTORS['Tom Cruise'])
    
elif searchActor == 'Penelope Cruz' : 
    print([ACTORS['Penelope Cruz']])
    
elif searchActor == 'Cameron Diaz' :
    print([ACTORS['Cameron Diaz']])
    
elif searchActor == 'Brad Pitt' :
    print(ACTORS['Brad Pitt'])
    
elif searchActor == 'Anthony Hopkins' : 
    print(ACTORS['Anthony Hopkins'])
    
elif searchActor == 'Jeremy Renner' :
    print(ACTORS['Jeremy Renner'])
    



    

    

