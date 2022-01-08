# Write a Python program to add member(s) in a set and iterate over it

s1 = {1, 2, 4, 5, 6}
print(type(s1))
print("Set is : ", s1)

s1.add(3)
s1.add((2, 3))
print("Adding Single elements Using add() in set : ", s1)

s1.update({2.3, 7, .9})
s1.update({(0, 9), 7.7})
print("Adding iterable elements Using update() in set : ", s1)
print(s1)
