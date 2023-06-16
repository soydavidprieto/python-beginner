def print_sorted_numbers(numbers):
    sorted_numbers = sorted(numbers)
    print("Sorted numbers:", sorted_numbers)

number_sequence = input("Enter a sequence of numbers (separated by spaces): ")

numbers_list = [int(number) for number in number_sequence.split()]

print_sorted_numbers(numbers_list)
