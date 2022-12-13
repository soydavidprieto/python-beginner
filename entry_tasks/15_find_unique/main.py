if __name__ == "__main__":
    numbers = input('Enter some numbers, separated by comma: ')
    my_set = set(int(number) for number in numbers.split(','))
    a = list(my_set)
    b = ', '.join(str(b) for b in a)
    print('Unique: ', b)
