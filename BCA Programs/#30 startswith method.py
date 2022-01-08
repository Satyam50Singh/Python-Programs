# WAP to check whether a string starts with specified characters.

str = input("Enter a string :")
ch = input("Enters characters :")

if(str.startswith(ch)) :
    print("Yes, String starts with", ch)
else :
    print("No, String doesnot starts with",ch)