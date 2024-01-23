num1 = (int(input("Please enter your first number for the calculation: ")))
num2 = (int(input("Please enter your second number for the calculation: ")))

sum = num1 + num2
diff = num1 - num2
diff2 = num2 - num1
prod = num1 * num2 
quot = num1 / num2
quot2 = num2 / num1
rema = num1 % num2
rema2 = num2 % num1

print(f"The Sum is {sum}")
print(f"The Difference is {diff} or {diff2}")
print(f"The Product is {prod}")
print(f"The Quotient is {quot} or {quot2}")
print(f"The Remainder is {rema} or {rema2}")
