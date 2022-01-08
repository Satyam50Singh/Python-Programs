# WAP to create a string from two given sting concatenating uncomman characters and values in a 
# given string.

str1 = input("Enter 1st string :")
str2 = input("Enter 2nd string :")

str1 = sorted(set(str1))
str2 = sorted(set(str2))

result = ""
for i in str1:
    if i not in str2:
        result +=i

for i in str2:
    if i not in str1:
        result +=i

print("Output - ",result)
