def print_third_elements(sequence):
    third_elements = sequence[2::3]
    print("Third elements:", third_elements)

sequence_input = input("Enter a sequence of characters: ")

print_third_elements(sequence_input)
