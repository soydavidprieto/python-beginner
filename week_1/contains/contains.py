if __name__ == '__main__':
    print('Task 9. Contains?')

word = input('Enter word: ')
letter = input('Enter letter: ')

# TODO: [Mykyta]: what about built-in operators? (https://realpython.com/python-in-operator/)
# Using magic methods (with double underscore) directly is sort of "dark magic",
# which should not be used unless you absolutely there is no other way.
# Extra useful reading (https://realpython.com/python-string-contains-substring/)
print(letter in word)
