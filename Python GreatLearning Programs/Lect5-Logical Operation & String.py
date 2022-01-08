#Lect5 - Logical Operation & String

##Logical Operations

#Operators

#  ==  :-  Equal to
#  !=  :-  Not equal to
#  >   :-  Greater than
#  <   :-  Less than
#  >=  :-  Greater than or equal to
#  <=  :-  Less than or equal to

#Equal to
x=12
y=12
print("x==y : ",x==y)
#Not equal to
print("x!=y : ",x!=y)

a=5
b=12
#Greater than
print("a>b : ",a>b)
#Less than
print("a<b : ",a<b)
#Greater than or equal to
print("a>=b : ",a>=b)
#Less than or equal to
print("a<=b : ",a<=b)

print('-------------------------------------------------')
##String : are used to store character sequence

String = "Data scientist"

print("\nSTRING : ",String)
print("Length of String : ",len(String))
print("First Char of String : ",String[0])
print("Print Character from 5th - 9th index : ",String[5:10])
print("String from 6th to the end : ",String[6:])
print("print from 2nd char to one char before last : ",String[1:-1])
print("Print String 3 times : ",String*3)
print("String Concatinaton :",String +" is cool!")
print("Concat : ",String[5:-4]+" TIST")

##String methods

print("String in Upper Case : ",str.upper(String))
print("String in Lower Case : ",str.lower(String))
print("String in Title Case : ",str.title(String))
