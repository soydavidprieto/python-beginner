from week_4.contacts.contact_list import ContactList
from week_4.contacts.contact import Contact
if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = ContactList()
    my_contact = Contact(name='Jack', email='jacke@xample.com', age=30)
    print(my_contact.name, my_contact.email, my_contact.age)
    my_contact1 = Contact(name='Jack', email='jacke@xample.com', age=30)
    my_contact1.email = "Dave"
    my_contact1.age = 35
    print(my_contact1.name, my_contact1.email, my_contact1.age)
    # contact_list.append_dict(my_contact)
    # contact_list.append_dict(Contact(name='Mary', email='jacke@xample.com', age=32))
    # contact_list.print_content()

