# Check if all items in the following tuple are the same.else

tuple1 = (45, 45, 45, 45)

t = tuple1[0]
val = 0

for i in tuple1:
    if i is i:
        val = 1
    else:
        val = 0
        break
print(True) if val else print(False)
