from week_4.contacts.contact_list import ContactList
from week_4.contacts.contact import Contact
if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = ContactList()
    contact = Contact(name='Jack', email='jacke@xample.com', age=30)
    contact_list.append(contact)
    contact_list.append(Contact(name='Maary', email='jacke@xample.com', age=32))
    contact_list.print_content()
    # contact
