if __name__ == '__main__':
    friends_total = int(input('How many friends do you have?: '))
    from collections import OrderedDict
    phone_book = OrderedDict()
    for n in range(friends_total):
        name = input("Please enter name of friend ({}): ".format(n + 1))
        phone = input("Please enter {}'s phone: ".format(name))
        print('Contact "{}" with phone "{}" created.'.format(name, phone))
        phone_book[name] = phone
    print('Your phone book:')
    for key, value in phone_book.items():
        print(f'{key}: {value}')
