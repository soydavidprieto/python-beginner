if __name__=='__main__':
    word = input('Type any word: ')
    letter = input('Type any letter: ')

    if letter in word:
        print("the word contains entered letter")
    else:
        print("letter not found")