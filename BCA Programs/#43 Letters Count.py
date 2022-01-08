# WAP to count Uppercase, Lowercase, special character& numeric values in a given string

str = input("Enter an string :")

u=0
l=0
s=0
n=0

for i in str:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isnumeric():
        n+=1
    else:
        s+=1

print("Uppercase :",u)
print("Lowercase :",l)
print("Numeric :",n)
print("specialcase :",s)