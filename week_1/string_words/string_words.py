def print_words(text):
    words = text.split()  # Split the text into a list of words
    for word in words:
        print(word)

# Prompt the user to enter text
text_input = input("Enter some text: ")

# Call the function to print the words
print_words(text_input)
