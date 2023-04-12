class Contact:
    def __init__(self):
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
        else:
            self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email!')
        else:
            self._email = email

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
            else:
                self._age = age
        except ValueError:
            raise ValueError('Invalid age!')
