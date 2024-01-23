num1 = (int(input("Please enter the First Number: ")))
num2 = (int(input("Please enter the Second Number: ")))
num3 = (int(input("Please enter the Third Number: ")))

if num1 > num2 and num1 > num3:
    print(f"The number {num1} is the biggest number")

elif num2 > num1 and num2 > num3:
    print(f"The number {num2} is the biggest number")

else:
    print(f"The number {num3} is the biggest number")