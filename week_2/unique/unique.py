string_list = []
int_list = []
while True:
    numbers = input("Enter your numbers separated by space or comma: ")
    if "," in numbers:
        numbers = numbers.replace(" ", "")
        string_list = numbers.split(",")
        int_list = [eval(i) for i in string_list]
        int_list.sort()
        print(type(string_list[0]))
        print(type(int_list[0]))
    elif " " in numbers:
        string_list = numbers.split()
        int_list = [eval(i) for i in string_list]
    else:
        print("Please enter you data correctly! ")
        continue
    my_set = set(int_list)
    int_list = list(my_set)
    int_list.sort()
    print(int_list)
    break
