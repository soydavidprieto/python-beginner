class ContactList:
    def __init__(self):
        self.contact_lst = []

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.contact_lst):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.contact_lst[index]

    def __str__(self):
        str_i = []
        for i in self.contact_lst:
            str_i.append((str(i)))
        return str(str_i

    # maximum = 3
    # contact = {
    #     'name': None,
    #     'email': None,
    #     'age': None
    # }
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     return self

    def append(self, contact):
        self.contact_lst.append(contact)

    # def print_content(self):
    #     for contact in self.contact_lst:
    #         print(f"name: {contact.name}, email: {contact.email}, age: {contact.age}, sex: {contact.sex}")
    #     # for contact in self.contact_lst_dict_approach:
    #     #     print(contact)

    # def append_dict(self, contact):
    #     new_contact = self.contact.copy()
    #     new_contact['name'] = contact.name
    #     new_contact['email'] = contact.email
    #     new_contact['age'] = contact.age
    #     new_contact['sex'] = contact.sex
    #     self.contact_lst_dict_approach.append(new_contact)
