from week_4.contacts.contact_list import ContactList
from week_4.contacts.contact import Contact
if __name__ == '__main__':
    print('Task 19. Contact List')

    my_list = ContactList()
    #print(id(my_list), id(ContactList))

    contact = Contact()
    mike = Contact()
    #print(id(contact), id(Contact))
    # print(contact.name, contact.email, contact.age, contact.sex)

    contact.name, contact.email, contact.age = "Andriy1", "qwerty@example.com1", 23
    mike.name, mike.email, mike.age = "Mike", "mike@gmail.com", 30
    # contact_list.append_dict(contact)
    # contact_list.print_content()
    my_list.append(contact)
    my_list.append(mike)

    print(my_list)

    for contact in my_list:
        print(contact)
