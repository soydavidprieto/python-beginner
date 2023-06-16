def print_coordinate(x, y, z):
    coordinate = f"({x}, {y}, {z})"
    print("Coordinate:", coordinate)

# Prompt the user to enter values for x, y, and z
x_input = input("Enter the value for x: ")
y_input = input("Enter the value for y: ")
z_input = input("Enter the value for z: ")

# Call the function to print the coordinate
print_coordinate(x_input, y_input, z_input)
