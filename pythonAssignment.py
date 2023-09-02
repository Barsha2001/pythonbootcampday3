def calculate_area(side_length):
    return side_length ** 2
try:
    side_length = float(input("Enter the length of a side of the square: "))
    if side_length >= 0:

        area = calculate_area(side_length)
        print(f"The area of the square with side length {side_length} units is {area} square units.")
    else:
        print("Please enter a non-negative value for the side length.")
except ValueError:
    print("Invalid input. Please enter a valid number for the side length.")
