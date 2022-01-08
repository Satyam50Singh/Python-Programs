# Program to get unique values from list.
lst = [1, 2, 1, 1, 3, 4, 4, 4, 3, 6, 4, 5]

temp = []
for i in lst:
    if i not in temp:
        temp.append(i)

print("Unique Values are:", temp)
