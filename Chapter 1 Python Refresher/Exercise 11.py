year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

q1 = year[-3]
print("Value at index -3:", q1)

q2 = year[::-1]
print("Original Tuple:", year)
print("Reversed Tuple:", q2)

q3 = year.count(2009)
print("Number of times 2009 appears in the tuple:", q3)

q4 = year.index(2018)
print("Index of 2018:", q4)

q5 = len(year)
print("Length of the tuple:", q5)