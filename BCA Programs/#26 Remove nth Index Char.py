#WAP to remove the nth index character from non-empty string.

str = input("Enter a string :")

index = int(input("Enter Index :"))


if(index <= len(str)): 
    temp=""
    for i in range(len(str)):
        if(i != index):
            temp+=str[i]
    print(temp)
else :
    print("Index is greater than string length")