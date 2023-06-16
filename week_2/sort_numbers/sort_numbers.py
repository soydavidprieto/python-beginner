def print_sorted_numbers(numbers):
    sorted_numbers = sorted(numbers)  # Sort the numbers
    print("Sorted numbers:", sorted_numbers)

# Prompt the user to enter a sequence of numbers
number_sequence = input("Enter a sequence of numbers (separated by spaces): ")

# Split the input into individual numbers and convert them to integers
numbers_list = [int(number) for number in number_sequence.split()]

# Call the function to print the sorted numbers
print_sorted_numbers(numbers_list)
