# WAP to add 'ing' at the end of a given string (length should be at least three). If the given string 
# already ends with 'ing then add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged

# str - 'abc'
# o/p - 'abcing' 

str = input("Enter a string :")

if(len(str) < 3):
    print(str)
else :
    if(str.endswith('ing')) :
        str+='ly'
    else :
        str+='ing'
    print("output :",str)
