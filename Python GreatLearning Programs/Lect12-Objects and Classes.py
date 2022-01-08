#Lect12 - Object and Classes

class Example :
    name =""    #Instance variables
    age=0
    def __init__ (self) : #Constructor
        print("Good morning.")
    def getinfo(self,name,age) : #mehod-1
        self.name = name
        self.age= age
    def showinfo(self) : #mehod-2 
        print("Name : ",self.name)
        print("Age :",self.age)
    toy=(lambda self,x,y :(x+y)**1/2)


E1=Example()    #Creating Object

E1.getinfo("Satyam Singh",19)  #method-1 Calling
E1.showinfo()       #method-2 Calling
print("(x+y)**1/2 ,x=6 & y=43 :",E1.toy(6,43))

