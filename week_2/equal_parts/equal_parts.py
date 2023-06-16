def split_sequence(sequence):
    length = len(sequence)
    middle_index = length // 2  # Find the index at the middle of the sequence

    if length % 2 == 0:  # If the length is even
        first_half = sequence[:middle_index]
        second_half = sequence[middle_index:]
    else:  # If the length is odd
        first_half = sequence[:middle_index + 1]
        second_half = sequence[middle_index:]

    return first_half, second_half

# Prompt the user to enter a sequence of characters
sequence_input = input("Enter a sequence of characters: ")

# Call the function to split the sequence
first_half, second_half = split_sequence(sequence_input)

# Print the split parts
print("First half:", first_half)
print("Second half:", second_half)
