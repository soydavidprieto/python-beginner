if __name__ == '__main__':
    input_list = input('List of numbers or letters, separated by comma: ') #3, 2, 1, 4, 5,  2, ss, q
    user_list = input_list.split(',')
    new_list = [item.strip() for item in user_list]
    every_2nd = new_list[2::2]
    print(every_2nd)
