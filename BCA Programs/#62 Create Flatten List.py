# Program to flatten a given nested list structure.

lst = [[10, 20], [50], [35, 3, 12], [232, 34], [90, 100], [232, 34]]

temp = []
for i in lst:
    temp.extend(i)

print("Flatten list: ", temp)
