# WAP to count repeated character in a string.

str = input("Enter an string : ")

temp = ""
for i in str :
    if i not in temp :
        if str.count(i) > 1 :
            print(i, "  ", str.count(i))
    temp += i