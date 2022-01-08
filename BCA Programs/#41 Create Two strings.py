# WAP to create two string from a given strings. Create the first string using those character which occur only once
# and create the second string which consists of multi-time occuring character in the said string .

str = input("Enter an string :")

str = sorted(str)

res1 = ""
res2 = ""

for i in str:
    if str.count(i) == 1:
        res1+=i
    else :
        res2+=i

print(res1,"  ", res2)
