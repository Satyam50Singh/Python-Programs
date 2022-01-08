# Write a program to convert a tuple into a number.

dummy = (91, 70, 32, 4)

num = 0
digit = 0
for i in dummy:
    digit = 0
    temp = i
    while i > 0:
        digit += 1
        i = i // 10
    num = num * (10 ** digit) + temp

print(num)
