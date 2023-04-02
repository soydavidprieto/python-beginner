from contact import contact, validate_name, validate_age, validate_email


if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = []

    while True:
        try:
            name = input('name: ')
            validate_name(name)

            email = input('email: ')
            validate_email(email)

            age = input('age: ')
            validate_age(age)
        except ValueError as e:
            print(e)
            continue

        new_contact = contact.copy()
        new_contact['name'] = name
        new_contact['email'] = email
        new_contact['age'] = age

        print('-' * 10)
        print(new_contact)
        print('-' * 10)

        contact_list.append(new_contact)
        proceed = input('add another one? (y/n): ')

        if proceed != 'y':
            break
