while True:
    while True:
        word = input("Please enter your word: ")
        letter = input("Please enter your letter: ")
        if letter in word:
            print(f"Your letter is present in the '{word}' word")
            break
        else:
            print(f"Your '{letter}' is NOT present in the the word '{word}'")
            continue
    exit = input("To to proceed, press any button, if you want to exit the program please press 'E', : ")
    if exit == "E" or exit == "e":
        break
    else:
        continue