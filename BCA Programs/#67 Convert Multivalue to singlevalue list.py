# Program to convert MultiValued List to single Values List.

lst = [10, 20, 30, [40, 50], 60, 70, [80, 90]]

res = []
for i in lst:
    if type(i) == list:
        res.extend(i)
    else:
        res.append(i)

print(res)
