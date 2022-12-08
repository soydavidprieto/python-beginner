if __name__ == '__main__':
    print("Hello! Let's split!\n")
    text = input('Type text:')
    size = len(text) + 1
    print(text[0:size//2], '|', text[size//2:])

