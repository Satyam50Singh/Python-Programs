# Write a Python program to get a string froma givenstringwhere all occurrences of its first char have been changedto'$',except the first char itself. 
# Sample String : 'restart' 
# Expected Result : 'resta$t'

str = input("Enter a string :")

temp=str[0]
for i in range(1, len(str)) :
    if(str[i] == str[0]):
        temp = temp + '$'
    else :
        temp = temp + str[i]
print(temp)
