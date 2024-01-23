import math

def square():
    side_length = float(input("Enter the side length of the square: "))
    area = side_length ** 2
    print("The area of the square is:", area)

def circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print("The area of the circle is:", area)

def triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

while True:
    print("Menu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    print("4: Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        square()
    elif choice == '2':
        circle()
    elif choice == '3':
        triangle()
    elif choice == '4':
        print("Thanks for using.")
        break
    else:
        print("Error: Incorrect input")