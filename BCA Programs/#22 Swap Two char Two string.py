# WAP to get a single string from two string , separated by space and swap the first two characters of
# each string
# string : 'abc', 'xyz'
# o/p - 'xyc abz'

str = input("Enter 1st string :")
str2 = input("Enter 2nd string :")

temp=""
for i in range(len(str)):
    if i==0 or i == 1:
        temp+=str2[i]
    else :
        temp+=str[i]
temp+=" "
for i in range(len(str2)):
    if i==0 or i == 1:
        temp+=str[i]
    else :
        temp+=str2[i]

print(temp)