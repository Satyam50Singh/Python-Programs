# Program to get the largest and second largest number from list

lst = []

print("Enter 6 no.s : ")

for i in range(6):
    a = int(input())
    lst.append(a)

print("List is :",lst)

lst.sort(reverse=True)
print(lst)

print("The largest number is :", lst[0])
print("The second largest number is :", lst[1])