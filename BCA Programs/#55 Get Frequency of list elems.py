# Program to get the frequency of the elements in a list.

lst = [1, 2, 1, 1, 3, 4, 4, 4, 3, 6, 4, 5]

unique_val = list(set(lst))
freq = []

for i in unique_val:
    freq.append([i, lst.count(i)])

print("Frequency of each unique elements :[value,frequency]\n", freq)
