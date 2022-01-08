#Lect11-Other Functions

##filter

data=[5,7,12,23,34,47,56,78,81,94]

              #here list() is used to store data in list data type
final_data = list(filter(lambda x: (x%2==0),data))
print(final_data)
##in filter() is used only boolean expressions .

##map
              #here tuple() is used to store data in tuple data type 
final_data2 = tuple(map((lambda x : x*12),data))
print("final_data2 : ",final_data2)

list1=[1,2,3,4]
list2=[2,4,5,6]

result_list=list(map((lambda x,y :x+y+2),list1,list2))
print("result_list : ",result_list)

##Reducer

#import , as both are keywords
#here functools and operator are a package or library
#f is an alias name of functools , o is for operator.
import functools as f
import operator as o

li = [5,10,15,20,25]
Sum=f.reduce(o.add,li)
print("Sum of all elements of li :- ",Sum)

##Accumulator.

import itertools as i

li_new =[1,2,3,5,6,7,9]

print("The summation of list is :",end="")
print(list(i.accumulate(li_new,lambda x,y: x+y)))


