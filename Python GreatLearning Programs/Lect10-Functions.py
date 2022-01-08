#Lect10-Functions

##Funtion : functions are the block of statement which is used to perform specific task. 
#function definition
def greet() :
	print("hii i am satyam\n")

greet() #function call

#example - 2
def addition(x,y):
	print("x :",x,"\ny :",y)
	print("Addition of x, y :",x+y,"\n")

addition(12,87.2)

#example - 3
def addition(x,y):
	print("x :",x,"\ny :",y)
	print("Addition of x, y :",x+y)
	if(x==y):
		print("both are equal")
	else :
		print("both were different.")

addition(12,23.2)
 
##Lambda function

#add two no.s using lambda
add= lambda x,y : x+y

print("Addition of 12 & 2 :",add(12,2))

#check no. is neg or pos.
#case-1
res= lambda num :num<0
if(res(12)):
    print("No. is -ve.")
else :
    print("No. is +ve.")
#case-2

num=-21
res= lambda : num<0
if(res()):
    print("No. is -ve.")
else :
    print("No. is +ve.")
