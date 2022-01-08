#Lect9-Loops

#Loops in python : for and while.

##for
#Example-1
print("For-Loop\n")
for name in ["Joe","Zoe","Brad","Angelia","Zuki","Thandi","Parsi"] :
    invite = "Hi "+name+", please help me!"
    print(invite)
#Example-2
data=[1,2,3,4,5]
for i in data :
    print(i)

##while
print("While Loop\n")
#Example-3
print("Number from 1-10.")

wish="Good Morning"
i=1;
while(i<=10):
    print(i,wish)
    i=i+1

##Get Values from user by using for loop and input method
li =[]
n=int(input("Enter the value of n : "))
print("Enter ",n," values :")
for i in range(n) :
    li.append(int(input()))
print(li)

##count nos bet 555 & 1111 which are divisible by 7

lis=[]
print("\nNos which are divisible 7 from 555-1111\n")
for x in range(555,1111) :
    if(x%7==0) :
        lis.append(x)
print(lis)
print("Total no.s :",len(lis))


print("\n\nPattern\n")
for i1 in range(1,6):
    print("*"*i1)
