sequence = list(input('Enter a sequence of characters:'))
my_list_lenght=len(sequence)
half_lenght=int(my_list_lenght/2)
first_half=sequence[:half_lenght]12
second_half=sequence[half_lenght:]
print(first_half, second_half)
