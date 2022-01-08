# WAP to calculate percentage of student

print("Enter marks : ")
sub1 = eval(input("Subject 1 : "))
sub2 = eval(input("Subject 2 : "))
sub3 = eval(input("Subject 3 : "))
sub4 = eval(input("Subject 4 : "))

print("\nMarks \n\nSubject 1 :", sub1,"\nSubject 2 :", sub2,"\nSubject 3 :", sub3,"\nSubject 4 :", sub4)

percentage = ((sub1+sub2+sub3+sub4)*100)/400

if(percentage > 85): 
    print("Excellent Performace \nPercentage is :", percentage)
elif percentage > 65 and percentage <=85 :
    print("Good Performace \nPercentage is :", percentage)
elif percentage > 34 and percentage <=65 :
    print("Fair Performace \nPercentage is :", percentage)
else :
    print("Bad Performace \nPercentage is :", percentage)
    
