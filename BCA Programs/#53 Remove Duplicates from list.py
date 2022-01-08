# Wap to remove duplicates from list.

list = [10, 20, 30, 10, 40, 30, 60, 50]

temp = []
for i in list:
    if i not in temp:
        temp.append(i)

print(temp)