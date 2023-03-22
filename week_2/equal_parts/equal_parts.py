input_string = input("Please enter your value: ")
first_part, second_part = input_string[:len(input_string)//2], input_string[len(input_string)//2:]
first_part, second_part = first_part.replace(",", ""), second_part.replace(",", "")
list_1 = first_part.split()
list_2 = second_part.split()

print(list_1, list_2)

