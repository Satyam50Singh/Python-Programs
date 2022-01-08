#Lect6 - Lists

#Lists : Lists can store Sequence of Objects
#        These Objects can be of different types.

mylist = ["Satyam",12,87.6,"Laptop"] #A string can have both string & number
print(type(mylist))
print("Values in mylist :",mylist)
print("Value at first position :",mylist[0])
print("Value at 3rd position :",mylist[2])
print("Value from 2nd and 3rd position :",mylist[1:3])
print("Type of List 3rd element : ",type(mylist[2]) )
print("Print list from 1st pos to end :",mylist[1:])

##list can be concat like strings
print("--------------------------------------------------------------")

a=[1,2,3,4,5]
b=['A','B','C','D','E']
c=["Delhi","Kolkata","Chennai","Goa"]
print("\na : ",a,"\nb :",b,"\nc :",c)
print("\nType of a :",type(a))
print("Concat list a & b : ",a+b)
d=a+b+c
print("Concat all lists in d : ",d)
print("print 5 last values of list d : ",d[-5:])

#length of list 
print("\nLength of List d :",len(d))

##Removing items from list
print("--------------------------------------------------------------")

#A object can be removed from a list by calling del(),remove(),pop() function.
new_list = ["Dehradun",12,90.02,"Sansar","Ramayan",12,'a',"Sansar"]
print("\nNew list : ",new_list)
#del() is used to delete entity on basis of index.
del(new_list[1])
print("After removing value at index 1 :",new_list)

#remove() is used to delete a specific entity.
new_list.remove("Sansar")
print("After removing Sansar from list :",new_list)

##Note : Only the first matching entry is removed

new_list.pop(2)
print("List after delete entity of index-2 : ",new_list)

##Checking for an instance of an element in a list.
print("--------------------------------------------------------------")
print("\nList :",new_list)
print("\nCheck 90.02 : ",90.02 in new_list)
print("Check 'Ram' : ","Ram" in new_list)

print("80 not in new_list : ",80 not in new_list)
print("Check 'Sansar' not in new_list : ","Sansar" not in new_list)

print("--------------------------------------------------------------")
##Check the maximum and minimum values in a list
list1=[12,4,5,32,-67,24,43]
print("List1 : ",list1)
print("Maximum value :",max(list1))
print("Minimum value :",min(list1))
#max() and min() functions will not works for strings in list

print("--------------------------------------------------------------")
##Appending an element to a list.
#Append() add a single element to the end of list
list1.append(900)
print("\nlist1 after appending 900 in it :",list1)

#extend() adds multiple elements to the end of list
list1.extend([56,89])
print("list1 after extending 56 and 89 in it :",list1)

#insert() add an element into a exact position
list1.insert(-1,787)
print("list1 after insert value 787 at index -1 :",list1)

print("--------------------------------------------------------------")
##Sorting list
#Sort()
data=[12,78,34,5,342,0,5,-3,343,1]
print("data :",data)
data.sort()
print("data in sorted order : ",data)

data1=[23,54,7,56,3.4,42]
print("\ndata1 :",data1)
print("sorted(data1) : ",sorted(data1)) #sorted() doesnot change original list
print("data1 : ",data1)

##Reassigning a list

data1[3]=78
print("\nReassigning the value of index-3 in a data1 : ",data1)
