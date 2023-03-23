if __name__ == '__main__':
    print('Task 15. Unique.')

inputs_list = input('Input:')
split_list = inputs_list.split(',')
int_list = list(map(int, split_list))

my_set = set((int_list))
# [Mykyta]: set(int_list), no extra brackets required, 
# python ignores those (1) is 1, but (1,) != 1, because (1,) a tuple in that case.

print('Unique:', my_set)
