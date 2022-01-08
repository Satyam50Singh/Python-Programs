#Check the gender of person

#short hand if
fruits = ["apple", "banana", "pomegranate" ]
if("apple" in fruits): print("\nYes! apple is available")

# short hand if else
ch = input("\nEnter your gender ('M' -> Male, 'F' -> Female) : ")

print("\nPerson is Male.") if(ch == 'M') else print("\nPerson is Female.")

#short hand if elif else
a=34
b=45
c=-34

print("a is the smallest number") if(a<b and a<c) else print("b is the smallest number")if(b<a and b<c) else print("c is the smallest number")
