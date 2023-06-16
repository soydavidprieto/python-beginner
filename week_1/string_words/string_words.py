def print_words(text):
    words = text.split()
    for word in words:
        print(word)

text_input = input("Enter some text: ")

print_words(text_input)
