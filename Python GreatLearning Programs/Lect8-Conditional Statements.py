#Lect8-Conditional Statements

##Conditional Statements : if, if else and elif

##if
a=12.7
if(a<15) :
    print("a is less than 15.\n")

#if else
str="Apple"
if(str=='Aplle') :
    print("If condition gets True")
    print("Both string are equal.")
else :
    print("If condition gets False")
    print("Both are different.")

##if elif else


a=12
b=89
c=45

#example 1
if(a>b and a>c):
    print("a is greater.")
elif(b>c) :
    print("b is greater")
else :
    print("c is greater")
#example 2
if(a==2 or b==5) :
    print("Emergency")
else :
    print("\nNormal")

