from contact import Contact

print('Task 19. Contact List')

contact = {
    'name': None,
    'email': None,
    'age': None
}

contact_list = []

while True:
    try:
        name = input('name: ')
        email = input('email: ')
        age = input('age: ')
    except ValueError as e:
        print(e)
        continue
        
    contact_inst = Contact(name, email, age)
    new_contact = contact.copy()
    new_contact['name'] = contact_inst.name
    new_contact['email'] = contact_inst.email
    new_contact['age'] = contact_inst.age

    print('-' * 10)
    print(new_contact)
    print('-' * 10)

    contact_list.append(new_contact)
    proceed = input('add another one? (y/n): ')

    if proceed != 'y':
        break