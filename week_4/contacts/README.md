# Task 19
You're asked to create contact list.

We already created [simple contact](https://github.com/mykytapavlov/python-beginner/tree/main/week_2/contact).

Static contact list could be created like that:

```python
contact = {
    'name': None,
    'email': None,
    'age': None
}

contact_list = []

jack = contact.copy()
jack['name'] = 'Jack'
jack['email'] = 'jack@example.com'
jack['age'] = 18

contact_list.append(jack)

mary = contact.copy()
mary['name'] = 'Mary'
mary['email'] = 'mary@example.com'
mary['age'] = 21
contact_list.append(mary)

for contact in contact_list:
    print(contact)

# We will see:
# {'name': 'Jack', 'email': 'jack@example.com', 'age': 18}
# {'name': 'Mary', 'email': 'mary@example.com', 'age': 21}
```

Now, since we create programs for other users, we want to accept contact info from them.
In simple world when users are careful and do only what you ask them to do, it's so easy!

```python
contact = {
    'name': None,
    'email': None,
    'age': None
}

contact_list = []

while True:
    name = input('name: ')
    email = input('email: ')
    age = input('age: ')

    new_contact = contact.copy()
    new_contact['name'] = name
    new_contact['email'] = email
    new_contact['age'] = age

    print('-' * 10)
    print(new_contact)
    print('-' * 10)

    contact_list.append(new_contact)
    proceed = input('add another one? (y/n): ')

    if proceed != 'y':
        break

# We will see:
# name: Jim
# email: jim@example.com
# age: 25
# ----------
# {'name': 'Jim', 'email': 'jim@example.com', 'age': '25'}
# ----------
# add another one? (y/n): n
```


Now, we asked to sort our contacts by age. In python, sort() may not work in case you mix types.
```python
age_list = [20, '21', 28, 19]
age_list.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'.
```

As well as we don't want to have users with negative age. 
Email should contain special characters like `@` and `.`.
Names should not be too large.

You see the problem, right? To be sure, lets implement it really quick.

```python
contact = {
    'name': None,
    'email': None,
    'age': None
}

contact_list = []

while True:
    name = input('name: ')
    if len(name) > 50:
        print('Name is too large!')
        continue

    email = input('email: ')
    if '@' not in email:
        print('Invalid email!')
        continue
    if '.' not in email:
        print('Invalid email!')
        continue

    age = input('age: ')
    try:
        # Python raises ValueError, when gets unexpected values by default!
        # int('a') -> ValueError: invalid literal for int() with base 10: 'a'
        age = int(age)
        if age <= 0:
            # We can force Python to raise an error (without extra message in this case)
            # when receive unexpected user input as well.
            raise ValueError
    except ValueError:
        print('Invalid age!')
        continue

    new_contact = contact.copy()
    new_contact['name'] = name
    new_contact['email'] = email
    new_contact['age'] = age

    print('-' * 10)
    print(new_contact)
    print('-' * 10)

    contact_list.append(new_contact)
    proceed = input('add another one? (y/n): ')

    if proceed != 'y':
        break
```

One of the problems here, that you may have a lot of fields/conditions to validate. 
At some point, you will have to move everything you have related to contact in separate file (`contact.py`)!
```python
# ./week_4/contacts/contact.py file
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
```

In program's entry point (`main.py`) we will use it like that:

```python
# ./week_4/contacts/main.py file
from contact import contact, validate_name, validate_age, validate_email


if __name__ == '__main__':
    print('Task 19. Contact List')

    contact_list = []

    while True:
        try:
            name = input('name: ')
            validate_name(name)

            email = input('email: ')
            validate_email(email)

            age = input('age: ')
            validate_age(age)
        except ValueError as e:
            print(e)
            continue

        new_contact = contact.copy()
        new_contact['name'] = name
        new_contact['email'] = email
        new_contact['age'] = age

        print('-' * 10)
        print(new_contact)
        print('-' * 10)

        contact_list.append(new_contact)
        proceed = input('add another one? (y/n): ')

        if proceed != 'y':
            break
```

Now, we moved things related to the contact into separate file. 
But we still have to call `validate_name`, `validate_email`, `validate_age`. 
What if we forget? What if other developer forget? 
What if there are too many validators which should be called in specific order?
How can we rely on such contact?
Can we save an instance of such contact to Database? Do we know which table to use?
Database may have strict schema for tables, invalid types are not allowed (and errors won't be user-friendly :).
Other team rely on your contact list? So, cascade errors may occur, and you'll have to fix it in the middle of the night!

Understanding the challenges, let's now hide the validation of the contact under the class definition 
(as well as everything else which is contact related).
Every other developer should not care about internals of our contact class.

1. Your task is it to rework `contact.py` in order to create `Contact` class 
and use it in `main.py` instead of current logic.
Look at [class](https://mykytapavlov.github.io/nerd/src/python/oop/class) once again.

2. You need to create `ContactList` class in `contact_list.py` and use it in `main.py` instead of default one.
```python
# 1. have to if it's an instance of Contact before append
contact_list = ContactList()
contact_list.append(1)  # -> ValueError('Invalid contact!')

contact = Contact(name='Jack', email='jack@example.com', age=30)
contact_list.append(contact)  # -> Save contact `Jack` to the storage

# 2. Support `for` loop
for contact in contact_list:
    print(contact)

# 3. print contact list nicely
print(contact_list)
```
