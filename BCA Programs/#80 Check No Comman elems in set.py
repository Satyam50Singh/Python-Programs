# Write a Python program to check if two given sets have no elements in common.

s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {13, 16, 17}

print('Yes')if s2.isdisjoint(s1) else print('No')
