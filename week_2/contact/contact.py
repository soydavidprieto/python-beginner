def print_info(name, age, address, phone):
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)
    print("Phone:", phone)

# Prompt the user to enter their information
name_input = input("Enter your name: ")
age_input = input("Enter your age: ")
address_input = input("Enter your address: ")
phone_input = input("Enter your phone number: ")

# Call the function to print the grouped information
print_info(name_input, age_input, address_input, phone_input)
