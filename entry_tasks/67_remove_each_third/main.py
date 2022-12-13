if __name__ == "__main__":
    a = input('Input some sequence of values, separated by comma: ')
    lst = a.split(',')
    del lst[2::3]
    for i in range(len(lst)):
        lst[i] = str.strip((lst[i]))
    print(lst)

