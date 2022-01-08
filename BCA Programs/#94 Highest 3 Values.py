# Write a Python program to find the highest 3 values in a dictionary.

d1 = {
    'a': 8,
    'b': 23,
    'c': 2,
    'd': 323,
    'e': 9
}

print("Highest 3 values : ", sorted(d1.values(), reverse=True)[:3])

# Write a Python program to get the top three items in a shop. Sample
data = {
    'item1': 45.50,
    'item2': 35,
    'item3': 41.30,
    'item4': 55,
    'item5': 24
}
print("Highest 3 items : ", sorted(data.values(), reverse=True)[:3])
