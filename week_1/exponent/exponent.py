while True:
    while True:
        x = input("Please enter your first number: ")
        if x.isdigit():
            while True:
                y = input("Please enter the number you want to exponent for: ")
                if y.isdigit():
                    print(f"The exponent of you first number is {int(x) ** int(y)}")
                    break
                else:
                    print("it seems you've entered wrong symbols, please try again< please note you have type digits")
                    continue
        else:
            print("it seems you've entered wrong symbols, please try again< please note you have type digits")
            continue
        break
    exit = input("To to proceed, press any button, if you want to exit the program please press 'E', : ")
    if exit == "E" or exit == "e":
        break
    else:
        continue