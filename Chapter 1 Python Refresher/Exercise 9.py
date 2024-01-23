list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Print list using for loop")

for item in list:
    print(item)

maxlist = max(list)
minlist = min(list)

print(f"Print largest number: {maxlist}")
print(f"Print smallest number: {minlist}")

list.sort()
print("Ascending order")
print(list)

list.sort(reverse=True)
print("Descending order")
print(list)

list.append(13)
list.append(62)

print("List after appending 13 and 62: ")
print(list)

