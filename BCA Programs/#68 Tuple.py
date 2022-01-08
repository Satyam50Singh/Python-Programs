# Tuple Operators, Functions, Properties

# Singleton Tuple
t = (2,)
print(t)
print(type(t))

# Creating a tuple
# way-1
t = tuple(range(10))
print(t)

# way-2
t1 = (1, 2, 3, 4, 5, 6, 'abc', 12.1, [12, 2, 3], {10, 20, 30})
print(t1)

# changes in tuple
t1 = list(t1)
t1[1] = 21
t1 = tuple(t1)
print(t1)

# Multiplication Operator
print(t*3)

# Concatenation
t1 = t1 + (121,)
print(t1)

# count() method
print("\nFrequencies of all elements\n")
for i in t1:
    print(i, " - - ", t1.count(i))

# index method
print("\nIndexes of all elements\n")
for i in t1:
    print(i, " - - ", t1.index(i))

T = ('Ram', 'Sita', 'Laxman', 'Ravan', 'Ram', 'Hanuman')
# print(T.index('Rams')) # Runtime Error - x not in tuple
T = T+('Shyam',)
print(T)

# Adding elements using slicing
T = T[:3] + ('Dashrath', 'kaushyla') + T[3:]
print(T)

# Remove element using slicing
T = T[:5] + T[6:]
print(T)
