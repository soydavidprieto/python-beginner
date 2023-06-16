def print_sorted_unique_numbers(numbers):
    unique_numbers = sorted(set(numbers))
    for number in unique_numbers:
        print(number)

number_sequence = input("Enter a sequence of numbers (separated by spaces): ")

numbers_list = [int(number) for number in number_sequence.split()]

print_sorted_unique_numbers(numbers_list)
