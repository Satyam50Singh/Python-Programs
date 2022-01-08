# String Operators

str1 = "Hello World!" # Assignment Operator
str2 = str1

if str1 == str2 : #Comparision operator
    print("Both string are equal")

str3 = "Hello! It's me" # Assignment Operator
str4 = "Namaste Ji"

if str3 != str4 : #Comparision operator
    print("Both string (3 & 4) are not equal")

if(str3 < str4) :#Comparision operator
    print("\nString str3 is earlier in alphabetic order, str3 - " + str3)

if(str3 > str4) :#Comparision operator
    print("\nString str4 is earlier in alphabetic order, str4 - " + str4)

for i in range(5):
    print(i*'*') #string multiplication operator

str5 = "Hii, I'm Ram, Studing in Sgrr Univerity"
str6 = "Ram"

print("Is Ram present in str5 : ", str6 in str5)

print("Is Ram not present in str5 : ", str6 not in str5)

print("Is str1 and str2 refer to same object : ", str1 is str2)

