# Program to find the avg of nested tuple

T = ((10, 10, 10, 12), (35, 34, 44, 98), (87, 12, 27, 43))

print(T)
sum = 0
avg = 0.0
l = []
for t in T:
    sum = 0
    for i in t:
        sum += i
    avg = sum/len(t)
    l.append(avg)

print(l)
