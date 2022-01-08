# WAP to convert a given string to all uppercase if it contains a least 2 uppercase character 
# in the first 4 character.

str = input("Enter a string :")

p=0
for i in range(0,4,1):
    if(str[i].isupper()) :
        p+=1

if(p>1) :
    print(str.upper())
else :
    print("Condition false.")

