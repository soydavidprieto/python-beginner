class ContactList:
    contact_lst = []

    def append(self, contact):
        self.contact_lst.append(contact)

    def print_content(self):
        for contact in self.contact_lst:
            print(f"name: {contact.name}, email: {contact.email}, age: {contact.age}")