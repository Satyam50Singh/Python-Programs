# Write a Python program to apply union, intersection, difference, symmetric difference operators on sets

s1 = {1, 3, 5, 'a', 7.7, 9, -23}
s2 = {'a', 6, 3, 5, 7.7, 's', 88}

# union operation
print("union operation")
temp = s1.union(s2)  # returns an resulted set
print("temp:", temp)

s1.update(s2)  # update existing set
print("set s1:", s1)

s1 = {1, 3, 5, 'a', 7.7, 9, -23}
s2 = {'a', 6, 3, 5, 7.7, 's', 88}

# intersection operation
print("\nintersection operation")
temp = s1.intersection(s2)  # returns an resulted set
print("temp:", temp)

s1.intersection_update(s2)  # update existing set
print("set s1:", s1)

s1 = {1, 3, 5, 'a', 7.7, 9, -23}
s2 = {'a', 6, 3, 5, 7.7, 's', 88}

# difference operation
print("\ndifference operation")
temp = s1.difference(s2)  # returns an resulted set
print("temp:", temp)

s1.difference_update(s2)  # update existing set
print("set s1:", s1)

s1 = {1, 3, 5, 'a', 7.7, 9, -23}
s2 = {'a', 6, 3, 5, 7.7, 's', 88}

# symmetric difference operation
print("\nsymmetric_difference operation")
temp = s1.symmetric_difference(s2)  # returns an resulted set
print("temp:", temp)

s1.symmetric_difference_update(s2)  # update existing set
print("set s1:", s1)
