# I did this project only with the basis I've learned from my course so far.

print("==================")
print("Area Calculator 📐")
print("==================")
print("Choose a shape to calculate its area:")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

choice = int(input("Which shape: "))
while choice < 1 or choice > 5:
    choice = int(input("Invalid choice. Please choose a number between 1 and 5: "))
if choice == 1:
    height = float(input("Enter the height of the triangle: "))
    base = float(input("Enter the base of the triangle: "))
    area = (height * base) / 2
    print(f"The area is {area}")
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area is {area}")
elif choice == 3:
    side = float(input("Enter the side length of the square: "))
    area = side**2
    print(f"The area is {area}")
elif choice == 4:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius**2
    print(f"The area is {area}")
elif choice == 5:
    print("Goodbye!")
