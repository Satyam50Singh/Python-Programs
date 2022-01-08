# WAP to reverse a string if it's length is multiple of 4.

str = input("Enter a string :")

if (len(str) % 4 == 0) :
    print(str[::-1])
else :
    print("string length is not multiple of 4.")