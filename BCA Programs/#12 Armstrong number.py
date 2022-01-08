#WAP to print armstrong number from range 1-1000

print("Armstrong numbers upto 1000 :")
for i in range(1, 1000):
    temp = i
    sum = 0
    while (temp > 0) :
        digit = int(temp%10)
        sum = sum + digit * digit * digit
        temp = int(temp/10)
    if sum == i:
        print(sum)

