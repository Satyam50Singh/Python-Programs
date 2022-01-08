# WAP to remove duplicates from a given string.

str = input("Enter an string :")
str = sorted(str)
res = ""
for i in str:
    if i not in res:
        res += i
print(res)