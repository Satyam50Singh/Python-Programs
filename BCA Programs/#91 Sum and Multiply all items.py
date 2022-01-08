# Write a Python program to sum and multiply all the items in a dictionary.

d = {
    'a': 10,
    'b': 7,
    'c': 2,
}

answer = 1

for i in d:
    answer = answer*d[i]

print(answer)
