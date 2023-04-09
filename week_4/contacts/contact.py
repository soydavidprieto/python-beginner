class Contact:

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

        if len(self.name) > 50:
            raise ValueError('Name is too large!')

        if '@' not in self.email or '.' not in self.email:
            raise ValueError('Invalid email!')

        try:
            self.age = int(self.age)  # Python will raise ValueError if not numeric
            if self.age <= 0:
                # We ask Python to raise ValueError if <= 0
                raise ValueError
        except ValueError:
            raise ValueError('Invalid age!')

