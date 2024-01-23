#Exercise 12
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


#Exercise 13
    
def prod(lst):
    product = 1
    for item in lst:
        product *= item
    return product

list = []


n = int(input("Enter the number of items you want to add to the list: "))
for i in range(n):
    item = float(input(f"Enter number {i + 1}: "))
    list.append(item)

if not list:
    print("The list is empty. Cannot calculate the product.")
else:
    product = prod(list)
    print("The product of the items in the list is:", product)