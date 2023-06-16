def split_sequence(sequence):
    length = len(sequence)
    middle_index = length // 2

    if length % 2 == 0:
        first_half = sequence[:middle_index]
        second_half = sequence[middle_index:]
    else:
        first_half = sequence[:middle_index + 1]
        second_half = sequence[middle_index:]

    return first_half, second_half

sequence_input = input("Enter a sequence of characters: ")

first_half, second_half = split_sequence(sequence_input)

print("First half:", first_half)
print("Second half:", second_half)
