# 14. Write a Python program to create a Caesar encryption. It is a type of substitution cipher in which each letter in the
# plaintext is replaced by a letter some fixed number of positions down the alphabet. 
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his
# private correspondence.

str = input("Enter an string :")

temp = ""
for i in str:
    a = ord(i)
    a = a-4
    temp+=chr(a)
print(temp)