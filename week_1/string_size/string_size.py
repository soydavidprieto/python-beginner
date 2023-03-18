while True:
    while True:
        s = input("Please enter your string: ")
        print(f"The stiring you've entered is '{s}', and it's lenghts is '{len(s)}'")
        break
    exit = input("To to proceed, press any button, if you want to exit the program please press 'E', : ")
    if exit == "E" or exit == "e":
        break
    else:
        continue