def print_third_elements(sequence):
    third_elements = sequence[2::3]  # Slice the sequence to get every third element
    print("Third elements:", third_elements)

# Prompt the user to enter a sequence of characters
sequence_input = input("Enter a sequence of characters: ")

# Call the function to print the third elements
print_third_elements(sequence_input)
