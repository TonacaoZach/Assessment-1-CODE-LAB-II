side1 = (int(input("Enter the length of the First side of the triangle: ")))
side2 = (int(input("Enter the length of the Second side of the triangle: ")))
side3 = (int(input("Enter the length of the Third side of the triangle: ")))

if side1 + side2 >= side3 and side1 + side3 >= side2 and side2 + side3 >= side1:
    print("You indeed have a triangle")

else:
    print("You do not have a triangle")

print("Type of triangle:")

if side1 == side2 == side3:
    print("You have an equalateral triangle")

elif side1 == side2 or side1 == side3 or side2 == side3:
    print("You have an isosceles triangle")

else:
    print("You have an scalene triangle")    