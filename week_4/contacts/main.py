from contact import Contact


if __name__ == '__main__':
    print('Task 19. Contact List')

    new_contacts = []
    while True:

        name = input('name: ')
        email = input('email: ')
        age = input('age: ')

        entered_contact = Contact(name, email, age)

        try:
            entered_contact.validate_name()
            entered_contact.validate_email()
            entered_contact.validate_age()
        except ValueError as e:
            print(e)

        new_contacts.append(entered_contact)
        print(entered_contact)

        proceed = input('add another one? (y/n): ')

        if proceed != 'y':
            break




