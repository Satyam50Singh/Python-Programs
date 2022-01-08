# WAP to check if a string contains all letters of the alphabet.

ch='y'

while ch == 'y' or ch == 'Y':
    str = input("Enter a string :")
    if(str.isalpha()):
        print("Yes, String has only characters.")
    else:
        print("No, String have others characters too.")
    ch = input("Do you want to check another string :")
