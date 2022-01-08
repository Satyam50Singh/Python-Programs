#WAP to print a check a number is prime or not.

import math
num = eval(input("Enter a number :"))

print("Number is :", num)

p=1

n=2
while(n<=num):
    if(num%n==0):
        p+=1
    n+=1
else :
    print("Checking ....")
    

if(p==2):
    print("\nYes, It's an prime number.")
else :
    print("\nNo, It's not an prime number.")
