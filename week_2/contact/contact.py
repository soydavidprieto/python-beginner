if __name__ == '__main__':
    print('Task 14. Contact.')


x = input('Enter your name:')
y = int(input('Enter your age:'))
z = input('Enter your address:')
c = input('Enter your phone:')

thisdict = {
    "name": x,
    "age": y,
    "address": z,
    "phone": c
}
print('Contact created', thisdict)
