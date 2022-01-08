#Wap to get the difference between the two list

list = [10, 20, 30, 10, 40, 30, 60, 50]
list2 = [4, 45, 23, 45, 89, 98, 32,5]

res = []
if len(list) == len(list2):
    for i in range(len(list2)):
        if list[i] > list2[i]:
            res.append(list[i] - list2[i])
        else:
            res.append(list2[i] - list[i])
    print("Difference of two list is :",res)
else:
    print("difference is not possible")
