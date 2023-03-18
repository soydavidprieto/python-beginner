words = []
while True:
    while True:
        text = input("Please enter your text: ")
        text = text.capitalize()
        words = text.split()
        print(f"Your text was split to te separate words in the list file '{words}' ")
        break
    exit = input("To to proceed, press any button, if you want to exit the program please press 'E', : ")
    if exit == "E" or exit == "e":
        break
    else:
        continue