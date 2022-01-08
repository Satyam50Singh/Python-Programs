# Write a Python script to merge two Python dictionaries.

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}


def MergeDict(dic1, dic2):
    return dic1.update(dic2)


MergeDict(dict1, dict2)
print(dict1)
