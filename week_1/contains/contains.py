if __name__ == '__main__':
    print('Task 9. Contains?')

word = input("Enter a word: ")
letter = input("Enter a letter: ")

if letter in word:
    print("The letter is in the word.")
else:
    print("The letter is not in the word.")
