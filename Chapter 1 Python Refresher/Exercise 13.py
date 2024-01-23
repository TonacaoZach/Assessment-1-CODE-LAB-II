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