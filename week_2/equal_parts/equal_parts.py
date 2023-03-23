if __name__ == '__main__':
    print('Task 12. Equal parts')


inputs_list = input('Enter sequence of characters:')
split_list = inputs_list.split(',')

list1 = list()
list2 = list()
result_list = list()

x = len(split_list)//2

list1 = split_list[0:x]
list2 = split_list[x:]

result_list.append(list1)
result_list.append(list2)

print('Result list', result_list)



