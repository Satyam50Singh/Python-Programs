# Program to remove kth element from list.
lst = []

print("Enter 5 values :")

for i in range(5):
    t = int(input())
    lst.append(t)

print("Original List :", lst)

k = int(input("Enter value of k :"))

if k < len(lst)-1:
    lst.pop(k)

print("Modified List :", lst)
