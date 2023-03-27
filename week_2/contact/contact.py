if __name__ == '__main__':
    print('Task 14. Contact.')
    my_dict={}
    n = input('Enter your name: ')
    age = input('Enter your age: ')
    address = input('Enter your address: ')
    ph = input('Enter your phone: ')

    my_dict = dict(name=n, age=age, address=address, phone=ph)
    print("Contact created: ", my_dict)