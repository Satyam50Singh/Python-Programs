# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 2

def sumElems(lis1):
    sum = 0
    for i in lis1:
        sum += i
    return sum


l = [12, 2, 34, 46, 7]

print("Sum : ", sumElems(l))
