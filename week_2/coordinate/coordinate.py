# the first approach
# x = input("Enter your X coordinate: ")
# y = input("Enter your Y coordinate: ")
# z = input("Enter your Z coordinate: ")
# list_transit = []
# list_transit.append(int(x)), list_transit.append(int(y)), list_transit.append(int(z))
# coordinate = tuple(list_transit)
# print(coordinate)
# print(type(coordinate))

# the second approach
list_transit = []
while True:
    a = input("Enter your coordinate: ")
    list_transit.append(int(a))
    if len(list_transit) < 3:
        continue
    else:
        coordinate = tuple(list_transit)
        print(coordinate)
        print(type(coordinate))
    break





