input_number = input("Please enter your numbers: ")
input_number = input_number.replace(" ", "")
numbers_list3 = input_number.split(",")
print(numbers_list3[0::2])