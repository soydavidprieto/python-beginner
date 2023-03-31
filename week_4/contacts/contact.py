contact = {
    'name': None,
    'email': None,
    'age': None
}


def validate_name(name):
    if len(name) > 50:
        raise ValueError('Name is too large!')


def validate_email(email):
    if '@' not in email or '.' not in email:
        raise ValueError('Invalid email!')


def validate_age(age):
    try:
        age = int(age)  # Python will raise ValueError if not numeric
        if age <= 0:
            # We ask Python to raise ValueError if <= 0
            raise ValueError
    except ValueError:
        raise ValueError('Invalid age!')


class Contact:
    # TODO: implement instead of above
    ...
