# Write a python program to count the number of string where the string length is 2 or more a
# and the first and last character are same from a given list of string

lst = ['abc', 'xyz', 'aba', '1221']

res = 0
for i in lst:
    if len(i) >= 2 and i[0] == i[len(i) - 1]:
        res += 1

print("Required Output-", res)
