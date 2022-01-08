num = eval(input("Enter a number :"))
print("Number is :", num)

temp = num
rev = 0
while(temp > 0):
    rev = rev*10+int(temp%10)
    temp = int(temp/10)
print("Reverse :",rev)

if(rev == num):
    print("YES")
else :
    print("NO")
    
