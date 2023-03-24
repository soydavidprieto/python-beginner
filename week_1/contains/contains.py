name = input('Enter name:\n')
letter = input('Enter letter: \n')
result=name.__contains__(letter)
print('Name contains this letter?',result)

# TODO: [Mykyta]: what about built-in operators? (https://realpython.com/python-in-operator/)
# Using magic methods (with double underscore) directly is sort of "dark magic",
# which should not be used unless you absolutely there is no other way.
# Extra useful reading (https://realpython.com/python-string-contains-substring/)
