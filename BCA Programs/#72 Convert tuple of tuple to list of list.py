# Write a python program to convert a given list of tuples to a list of lists.

temp = [(1, 2), (2, 3), (3, 4)]

lists = []
l = []
for i in temp:
    l = []
    for j in i:
        l.append(j)
    lists.append(l)

print(lists)
