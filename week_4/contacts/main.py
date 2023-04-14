from week_4.contacts.contact_list import ContactList
from week_4.contacts.contact import Contact
if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = ContactList()
    contact = Contact(sex="female")
    contact_list.append(contact)
    print(contact.name, contact.email, contact.age, contact.sex)
    contact.name, contact.email, contact.age = "Andriy", "qwerty@example.com", 22
    contact_list.append_dict(contact)
    contact_list.append(Contact(sex="male"))
    contact_list.print_content()


