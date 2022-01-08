# WAP to get a string made of the first 2 & the last 2 chars from a given a string.
# IF the string length is less than 2, return instead of the empty string.
# str - 'abcdefghij'
# o/p - 'abij'

str = input("Enter a string :")

size = len(str)

if(size < 2) :
    print("Empty string.")
else :
    s = str[:2] + str[-2:: 1]
    print(s)