row = int(input("Enter the number of rows you want for the output: "))

for i in range(1, row + 1):
    print(*range(1, i + 1))