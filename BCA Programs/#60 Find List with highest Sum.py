# Program to find the list in a list of lists whose of element is highest

lst = [[1, 2, 3], [4, 5, 6], [10, -11, 12], [7, 8, 9]]

max = 0
sum = []
temp = 0
for i in lst:
    temp = 0
    for j in i:
        temp += j
    if max < temp:
        sum = []
        max = temp
        sum.extend(i)

print("List with maximum sum :", sum)
