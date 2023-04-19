from week_4.contacts.contact_list import ContactList
from week_4.contacts.contact import Contact
if __name__ == '__main__':
    print('Task 19. Contact List')

    my_list = ContactList()
    contact = Contact(sex="female")
    contact.name, contact.email, contact.age = "Andriy", "qwerty@example.com", 35
    my_list.append(contact)
    print(contact.name,contact.email, contact.age, contact.sex)
    #contact.email = "qwerty"
    #contact_list.append(Contact(name='Mary', email='jacke@xample.com', age=32))
    my_list.print_content()
    #contact.name, contact.email, contact.age = "Andriy", "qwerty@example.com", -1
    for contact in my_list:
        print(contact)