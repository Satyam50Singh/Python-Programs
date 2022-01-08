#Program to print only even numbers from 1-100.

num = 1
while(num <= 100):
    if(num%2 == 0):
        if(num == 100):
            print(num , " ", " ")
        else :
            print(num , sep=" ", end=" ")
    else :
        pass
    num+=1
    
