class ContactList:
    contact_lst = []
    contact = {
        'name': None,
        'email': None,
        'age': None
    }

    def append(self, contact):
        self.contact_lst.append(contact)

    def print_content(self):
        # for contact in self.contact_lst:
        #     print(f"name: {contact.name}, email: {contact.email}, age: {contact.age}")

        for contact in self.contact_lst:
            print(contact)

    def append_dict(self, contact):
        new_contact = self.contact.copy()
        new_contact['name'] = contact._name
        new_contact['email'] = contact._email
        new_contact['age'] = contact._age
        self.contact_lst.append(new_contact)

