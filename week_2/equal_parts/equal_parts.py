if __name__ == '__main__':
    print('Task 12. Equal parts')
    my_list=[3, 2, 1, 4, 5,  2, "ss", "q", 9]

    my_list_length = len(my_list)
    n=int(my_list_length/2)

    my_list2=my_list[0:n]
    my_list3=my_list[n:]

    print(my_list2, my_list3)