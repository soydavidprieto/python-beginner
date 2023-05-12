import random

a_list = [['*', '*', '*', '*'], ['*', ' ', ' ', '*'], ['*', ' ', ' ', '*'], ['*', '*', '*', '*']]
indices = []


for ind_x, x in enumerate(a_list):
    for idx_y, y in enumerate(x):
        if y == " ":
            indices.append((ind_x, idx_y))
# for x in a_list:
#     for y in x:
#         if y != "*" and y != "o" and y != "$":
#             indices.append((a_list.index(x), x.index(y)))
new_apple = random.randrange(len(indices))
abc = a_list[new_apple]
print(indices)
print(abc)
