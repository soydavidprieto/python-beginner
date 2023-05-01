class ContactList:
    def __init__(self):
        self.contact_list = []

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= len(self.contact_list):
            raise StopIteration
        n = self.n
        self.n += 1
        return self.contact_list[n]

    def __str__(self):
        str_cont = []
        for cont in self.contact_list:
            str_cont.append(str(cont))
        return str(str_cont)

    def append(self, contact):
        self.contact_list.append(contact)

    # def print_contact(self, contact_list):
    #     for contact in contact_list:
    #         print(contact)

# class AddressBook(list):
#     def add_contact(self, *args, **kwargs):
#         new_contact = Contact(*args, **kwargs)
#         self.append(new_contact)
#
#     def display_contacts(self):
#         for contact in self:
#             print(contact)
#
# contacts = AddressBook()
# contacts.add_contact("Adam Smith", "adam@email.com")
# contacts.add_contact("Bob Jones", "bob@email.com")
# contacts.add_contact("Charlie Doe", "charlie@email.com")
# contacts.display_contacts()
#
# class PowTwo:
#     """Class to implement an iterator
#     of powers of two"""
#
#     def _init_(self, max=0):
#         self.max = max
#
#     def _iter_(self):
#         self.n = 0
#         return self
#
#     def _next_(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration