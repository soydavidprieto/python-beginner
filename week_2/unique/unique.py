string_list = []
int_list = []
amount = {}
while True:
    numbers = input("Enter your numbers separated by space or comma: ")
    if "," in numbers:
        numbers = numbers.replace(" ", "")
        string_list = numbers.split(",")
        int_list = [eval(i) for i in string_list]
    elif " " in numbers:
        string_list = numbers.split()
        int_list = [eval(i) for i in string_list]
    else:
        print("Please enter you data correctly! ")
        continue
    my_set = set(int_list)
    list_unique = list(my_set)
    list_unique.sort()
    print(list_unique)
    for i in string_list:
        amount[i] = string_list.count(i)
    print(amount)
    occurrences = 0
    for x, y in amount.items():
        if y > 1:
            occurrences = occurrences + 1
    print(f"The occurrences are enumerated:   {amount}" )
    print(f"Tme amount of elements that are occurring is   {occurrences}")
    break

