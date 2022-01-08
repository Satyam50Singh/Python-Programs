# Write a Python Program to check if a specified element presents in a tuple of tuples

demo = (('Red', 'White', 'Blue'), ('Green', 'Pink',
        'Purple'), ('Orange', 'Yellow', 'Lime'))

test = input("Enter color to check :- ")

p = 0
for i in demo:
    if test in i:
        p = 1
print(test, "present in a tuple") if p == 1 else print(
    test, "not present in a tuple")
