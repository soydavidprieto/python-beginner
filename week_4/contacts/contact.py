
class Contact:
    def __init__(self):
        self._name = None
        self._email = None
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age.lstrip('-+').isdigit():
            if int(age) > 0:
                self._age = int(age)
            else:
                raise ValueError('Age is less or equal 0')
        else:
            raise ValueError(f'Incorrect type for age: {age}. Expected: <class \'int\'>, got: {type(age)}')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) < 50:
            self._name = name
        else:
            raise ValueError(f'Name is too large!')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email!')
        else:
            self._email = email

    def __str__(self):
        return f"added contact: ({self._name},{self._email},{self._age})"

    ...
