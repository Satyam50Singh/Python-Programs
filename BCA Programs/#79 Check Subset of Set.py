# Write a Python program to check if a set is a subset of anotherset

s1 = {1, 2, 3, 4, 5, 6, 7}
sub_s1 = {3, 6, 7}

print('Yes')if sub_s1.issubset(s1) else print('No')
