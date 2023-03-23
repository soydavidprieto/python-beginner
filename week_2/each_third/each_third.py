if __name__ == '__main__':
    print('Task 11. Each third')


inputs_list = input('Enter sequence of characters:')
split_list = inputs_list.split(',')

i = 0
new_list = list()
while i < len(split_list):
    new_list.append(split_list[i])
    i = i + 2

print('Result list', new_list)


# [Mykyta]: Actually nice :)
# (but the task was to get a bit more familiar with slices using step)
# FYI, https://realpython.com/lessons/string-slicing/
