def print_sorted_unique_numbers(numbers):
    unique_numbers = sorted(set(numbers))  # Convert to set to get unique numbers, then sort the set
    for number in unique_numbers:
        print(number)

# Prompt the user to enter a sequence of numbers
number_sequence = input("Enter a sequence of numbers (separated by spaces): ")

# Split the input into individual numbers and convert them to integers
numbers_list = [int(number) for number in number_sequence.split()]

# Call the function to print the sorted unique numbers
print_sorted_unique_numbers(numbers_list)
