#Lect7-Tuple,Dictionaries and Sets    

##Tuple :Tuple are just similar as list but we cannot append or extend data in it.
##       Tuple are immutable.

my_tuple = (12,"Stanford",'z',"Japan",78.67,56)
print("\nmy_tuple :",my_tuple)
print("\nType of my_tuple :",type(my_tuple))
print("Element at Index 0 :",my_tuple[0])
print("my_tuple[1:4] :",my_tuple[1:4])
print("my_tuple[-3] :",my_tuple[-3])

##Dictionaries : is a type of collection which consists of key ,value pairs
               #A dictionary is indexed through keys.The key and values are of any type.
my_dict = {"Apple":12,"name":"Satyam","age":19}
print("\nmy_dict : ",my_dict)
print("\ntype(my_dict) :",type(my_dict))
print("Value at key 'name' : ",my_dict['name'])
print("Value at key 'age' : ",my_dict['age'])
print("Length of my_dict :",len(my_dict))

##Sets :A Sets is an unordered pair of data type is iterable,mutable and has no duplicate elements.

s={1,1,3,45,"Sat",'Rat',"Lion",'Lion'}
print("\ns :",s)
print("type(s) :",type(s))

##we cannot access any element in set through indexing.
