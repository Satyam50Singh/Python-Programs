# Program to convert the list of multiple integer into a single integer

lst = [10, 78, 64, 1, 438]

num = 0
digit = 0
for i in lst:
    temp = i
    digit = 0
    while(temp > 0):
        digit += 1
        temp = temp // 10
    num = num * (10**digit) + i

print("Req. Output :", num)
