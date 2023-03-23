if __name__ == '__main__':
    print('Task 15. Unique.')

inputs_list = input('Input:')
split_list = inputs_list.split(',')
int_list = list(map(int, split_list))

my_set = set((int_list))

print('Unique:', my_set)
