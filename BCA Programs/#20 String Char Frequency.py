# WAP to count the number of characters (character frequency) in a string

str = input("Enter a string :")

temp = ""
print("\nFrequencies and Characters :\n")
for i in str :
    if(i not in temp) :
        print(i , "  " , str.count(i))
    temp += i
