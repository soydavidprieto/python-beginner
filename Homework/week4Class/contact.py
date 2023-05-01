class Contact:
    def __init__(self):
        self._name = None
        self._email = None
        self._age = None

    def __str__(self):
        return f'name: {self.name} email: {self.email} age: {self.age}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.capitalize()
        if len(name) > 50:
            raise ValueError('Name is too large!')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email!')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        try:
            self._age = int(age)  # Python will raise ValueError if not numeric
            if int(age) <= 0:
                # We ask Python to raise ValueError if <= 0
                raise ValueError
        except ValueError:
            raise ValueError('Invalid age!')

# cont_name = input('Name: ')
# cont_email = input('Email: ')
# cont_age = input('Age: ')


# new_cont = Contact()
# new_cont.name = "bguis"
# new_cont.email = "bgusi@nvuis.g"
# new_cont.age = 75
# print(f'Name: {new_cont.name}, Email: {new_cont.email}, Age: {new_cont.age}')


