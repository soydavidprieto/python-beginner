full_list = list(input("Enter the sequence of characters: "))
first_half = full_list[:len(full_list)//2]
second_half = full_list[len(full_list)//2:]
print(first_half, second_half)