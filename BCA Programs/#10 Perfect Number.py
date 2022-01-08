num = eval(input("Enter a number :"))
print("Number is :", num)

sum=0
for i in range(1, num):
    if (int(num%i) == 0):
        sum = sum + i

if num == sum :
    print("Yes")
else :
    print("No")
