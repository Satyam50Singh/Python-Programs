# Program to replace the last element of first list by another list.

l1 = [10, 20, 30, 40, 50]
l2 = [90, 98, 989]

l1.pop()
l1.extend(l2)

print(l1)
