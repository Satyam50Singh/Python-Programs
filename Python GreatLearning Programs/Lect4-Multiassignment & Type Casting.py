#Lect4 - MultiAssignment and Type Casting

## MultiAssignment
#Assign different values in different variables
a,b,c=5,6,7
print('a = ',a,'\nb = ',b,'\nc = ',c)
d=a+b+c
print("Addition of three values : ",d)

#Assign same value in different variables
a1=b1=c1=15
print('a1 = ',a1,'\nb1 = ',b1,'\nc1 = ',c1)

## Type Casting

#int to float

val=78
print("Value of val : ",val)
print("type of val = ",type(val))
val=float(val)
print("Value of val : ",val)
print("type of val = ",type(val))

#float to int

val1=7.18
print("\nValue of val1 : ",val1)
print("type of va1l = ",type(val1))
val1=int(val1)
print("Value of val1 : ",val1)
print("type of val1 = ",type(val1))

#int/float to str

data=78.9
print("\nValue of data : ",data)
print("type of data = ",type(data))
data=str(data)
print("Value of data : ",data)
print("type of data = ",type(data))
data1=65
print("\nValue of data1 : ",data1)
print("type of data1 = ",type(data1))
data1=str(data1)
print("Value of data1 : ",data1)
print("type of data1 = ",type(data1))

## str to int is not possible

#bool to int 
res= True
print("\nResult : ",res)
print("type of res : ",type(res))
res=int(res)
print("Value of res :",res)
print("type of res : ",type(res))

#bool to str

res1= True
print("\nResult : ",res1)
print("type of res1 : ",type(res1))
res1=str(res1)
print("Value of res1 :",res1)
print("type of res1 : ",type(res1))

#int to bool
x=0
print("\nValue of x : ",x)
print("type of x : ",type(x))
x=bool(x)
print("Value of x : ",x)
print("type of x : ",type(x))
