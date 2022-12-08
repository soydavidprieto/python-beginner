if __name__ == '__main__':

    values = input("Input some integers separated by comma: ")
    a = values.split(',')
    b = ([int(b) for b in a])
    c = sorted(b)
    print(c)
