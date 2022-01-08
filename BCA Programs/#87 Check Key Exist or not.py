# Write a Python script to check whether a given key already exists in a dictionary.

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key = 5
value = 56

print("key: ", key, ", Exists") if key in dic.keys(
) else print("key: ", key, ", Not Exist! :(")
