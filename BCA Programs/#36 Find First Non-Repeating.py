# WAP to find the first non-repeating characters.

str = input("Enter an string :")

for i in str :
    if str.count(i) == 1 :
        print("Non repeating character is :",i)
        break