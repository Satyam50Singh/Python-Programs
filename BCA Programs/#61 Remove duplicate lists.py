# Program to remove duplicates from list of lists
lst = [[10, 20], [50], [35, 3, 12], [232, 34], [90, 100], [232, 34]]

print("Original List :", lst)

temp = []
for i in lst:
    if i not in temp:
        temp.append(i)

print("Required List :", temp)
