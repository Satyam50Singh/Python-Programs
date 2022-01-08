# Write a Python script to add a key to a dictionary. Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

d1 = {0: 10, 1: 20}
# Add single element
d1[3] = 30
print(d1)

# add multiple elements
d1.update({4: 40, 5: 50})
print(d1)
