# Program to find comman items from two lists.
s1 = "Today is Sunday , Good Morning"
s2 = "Tomorrow is Monday , Good Night"
lst1 = s1.split()
lst2 = s2.split()

res = []
for i in lst1:
    if i in lst2:
        res.append(i)

print("Comman Items from lst1 & lst2 :",res)
