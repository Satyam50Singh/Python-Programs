N = int(input("ENTER VALUE OF N:"))

p = 0
x = 1
while p < N:
    t = 3*x+5
    if t % 5 != 0:
        print(t)
        p += 1
    x += 1
