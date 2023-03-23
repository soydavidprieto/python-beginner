if __name__ == '__main__':
    print('Task 10. Sort numbers')

inputs_list = input('Enter list of digits:')
split_list = inputs_list.split(',')
int_list = list(map(int, split_list))
int_list.sort()

print('Ordered list:', int_list)

