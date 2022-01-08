# WAP to remove consecutive duplicates of a given list.

lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 9, 5, 5, 3, 3, 112]
res = []
for i in range(len(lst)):
    if i != (len(lst)-1):
        if lst[i] != lst[i+1]:
            res.append(lst[i])

res.append(lst[len(lst)-1])

print("Req. List :", res)
