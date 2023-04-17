

class Contact:
    def _init_(self):
        self._name = None
        self._email = None
        self._age = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 50:
            raise ValueError('Name is too large!')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email!')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        try:
            age = int(age)  # Python will raise ValueError if not numeric
            if age <= 0:
                # We ask Python to raise ValueError if <= 0
                raise ValueError
        except ValueError:
            raise ValueError('Invalid age!')

# cont_name = input('Name: ')
# cont_email = input('Email: ')
# cont_age = input('Age: ')


new_cont = Contact()
new_cont.name = "bguis"
new_cont.email = "bgusi@nvuis.g"
new_cont.age = 75
print(f'Name: {new_cont.name}, Email: {new_cont.email}, Age: {new_cont.age}')


