#Exercise 2
import numpy as np

# Define the array
original_array = np.array([20, 23, 82, 40, 32, 15, 67, 52])

# Find the indices of even numbers
even_indices = np.where(original_array % 2 == 0)
print("Indices of even numbers:", even_indices)

# Sort the array
sorted_array = np.sort(original_array)
print("Sorted array:", sorted_array)

# Slice elements from index 3 to the end of the array
sliced_array1 = original_array[3:]
print("Slice from index 3 to the end:", sliced_array1)

# Slice elements from index 0 to index 4
sliced_array2 = original_array[:5]
print("Slice from index 0 to index 4:", sliced_array2)

# Print [32 15 67] using negative slicing
negative_sliced_array = original_array[-5:-2]
print("Negative slicing to print [32 15 67]:", negative_sliced_array)


#Exercise 3

import operator

def add(x, y):
    return operator.add(x, y)

def subtract(x, y):
    return operator.sub(x, y)

def multiply(x, y):
    return operator.mul(x, y)

def divide(x, y):
    if y != 0:
        return operator.truediv(x, y)
    else:
        return "Cannot divide by zero!"

def modulus(x, y):
    if y != 0:
        return operator.mod(x, y)
    else:
        return "Cannot perform modulus with zero!"

def check_greater(x, y):
    return operator.gt(x, y)

def calculator():
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Check greater number")
        print("Q. Quit")

        choice = input("Enter your choice (1-6 or Q to quit): ").upper()

        if choice == 'Q':
            print("Calculator closed. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                x = float(input("Enter first value: "))
                y = float(input("Enter second value: "))
                
                if choice == '1':
                    result = add(x, y)
                elif choice == '2':
                    result = subtract(x, y)
                elif choice == '3':
                    result = multiply(x, y)
                elif choice == '4':
                    result = divide(x, y)
                elif choice == '5':
                    result = modulus(x, y)
                elif choice == '6':
                    result = check_greater(x, y)

                print("Result:", result)

            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please enter a number from 1 to 6 or Q to quit.")

if __name__ == "__main__":
    calculator()
