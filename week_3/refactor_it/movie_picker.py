GENRES = dict()
GENRES['1'] = {'gender': 'comedy', 'title': 'Meet the Parents'}
GENRES['2'] = {'gender': 'comedy', 'title': 'Anger Management'}
GENRES['3'] = {'gender': 'adventures', 'title': 'Mummy'}
GENRES['4'] = {'gender': 'romantic', 'tittle': 'Vanilla Sky'}
GENRES['5'] = {'gender': 'romantic', 'title': 'Meet Joe Black'}
GENRES['6'] = {'gender': 'drama', 'tittle': 'Meet Joe Black'}
GENRES['7'] = {'gender': 'thriller', 'tittle': 'Vanilla Sky'}
GENRES['8'] = {'gender': 'action', 'tittle': 'Mission Impossible'}

result = dict()


# Task 18
def search_data():
    try:
        key = raw = input('Please Input Search Criteria:')
        for k, subdict in GENRES.items():
            if key == subdict['gender']:
                return k, subdict  # return key and the sub-dictionary
    except TypeError:
        print('Wrong data type proveided as an argument')


print(search_data())