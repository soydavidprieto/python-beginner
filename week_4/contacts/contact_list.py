class ContactList:
    def __init__(self):
        self.contact_lst = []
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.contact_lst)

    # contact = {
    #     'name': None,
    #     'email': None,
    #     'age': None
    # }

    def append(self, contact):
        self.contact_lst.append(contact)

    def print_content(self):
        for contact in self.contact_lst:
            print(f"name: {contact.name}, email: {contact.email}, age: {contact.age}, sex: {contact.sex}")

        # for contact in self.contact_lst:
        #     print(contact)
    #
    # def append_dict(self, contact):
    #     new_contact = self.contact.copy()
    #     new_contact['name'] = contact.name
    #     new_contact['email'] = contact.email
    #     new_contact['age'] = contact.age
    #     self.contact_lst.append(new_contact)

