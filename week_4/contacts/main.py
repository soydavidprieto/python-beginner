from contact import Contact


if __name__ == '__main__':
    print('Task 19. Contact List')

    new_contacts = []
    while True:

        name = input('name: ')
        email = input('email: ')
        age = input('age: ')

        entered_contact = Contact()
        entered_contact.name = name
        entered_contact.age = age
        entered_contact.email = email

        new_contacts.append(entered_contact)
        print(entered_contact)

        proceed = input('add another one? (y/n): ')

        if proceed != 'y':
            break




