from contact import Contact
from contactList import ContactList

if __name__ == '__main__':
    print('Task 19. Contact List')
    contact_list = ContactList()
    jack = Contact()
    jack.name = 'Jack'
    jack.email = 'jack@example.com'
    jack.age = 30
    contact_list.append(jack)
    joanna = Contact()
    joanna.name = 'joanna'
    joanna.email = 'joanna@example.com'
    joanna.age = 18
    contact_list.append(joanna)
    proceed = 'y'
    while proceed == 'y':
        try:
            contact = Contact()
            contact.name = input('name: ')
            contact.email = input('email: ')
            contact.age = input('age: ')
            # new_contact = f'Name: {contact.name}; Email: {contact.email}; Age: {contact.age}'
            contact_list.append(contact)
            print(contact_list)
            for contacts in contact_list:
                print(contacts)
            # contact_list.print_contact(contact)

        except ValueError as e:
            print(e)
            continue
        proceed = input('add another one? (y/n): ')
        if proceed != 'y':
            break
