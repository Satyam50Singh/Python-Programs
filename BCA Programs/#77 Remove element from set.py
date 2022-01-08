# Write a Python program to remove an item from a set if it is present in the set

s1 = {'a', 'b', 'c', 'd', 'e', 'f'}
print("Set is : ", s1)

s1.remove('b')  # if element not present then it will raise an runtime error
# if element not present then it will not raise an runtime error
s1.discard('s')

s1.pop()
print("Set is : ", s1)

s1.clear()
print("After clear, Set is : ", s1)

del s1
