if __name__ == '__main__':
    print('Task 12. Equal parts')
    my_list = [1, 5, 7, 3, 6, 9, 2, 6, 4]
    my_list_length = len(my_list)
    print(my_list_length)
    #my_list1 = int(my_list_length/2)
    my_list1 = my_list_length //2
    print(my_list1)
    sub_sequence = my_list[:my_list1]
    print(sub_sequence)
    sub_sequence = my_list[my_list1:]
    print(sub_sequence)
