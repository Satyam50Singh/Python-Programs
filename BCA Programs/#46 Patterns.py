print("Language - Python")
print("Developer - Satyam Singh")
print("Date & Day - 0ct 25, 2021 Monday")
print("\n                   Multi-Patterns")
N = 5
num = 1
ch = 65
ch2 = 97
print("---------------------------------------------------------")
for i in range(N):
    print("| ", end="")
    for j in range(-1,i):
        print("*", end=" ")
    for l in range(N,i,-1):
        print(" ", end=" ")
    print("| ", end="")
    for k in range(-1, i):
        print(num, end=" ")
        num+=1
    for l in range(N,i,-1):
        print(" ", end=" ")
    print("| ", end="")
    for k in range(-1, i):
        print(chr(ch), end=" ")
        ch+=1
    for l in range(N,i,-1):
        print(" ", end=" ")
    print("| ", end="")
    for j in range(-1,i):
        if j%2 == 0:
            print(num, end=" ")
        else:
            print(chr(ch2), end=" ")
            ch2+=1
    for l in range(N,i,-1):
        print(" ", end=" ")
    print("| ", end="")
    print()
    num=1
    ch = 65
    ch2 = 97

num = N
num2 = N
ch = 65
print("---------------------------------------------------------")
for i in range(N):
    print("| ", end="")
    for j in range(N-1, i, -1):
        print(" ", end=" ")
    for k in range(-1,i):
        print("@", end=" ")
    print(end="  ")
    print("| ", end="")
    for j in range(N-1, i, -1):
        print(" ", end=" ")
    for k in range(-1,i):
        print(num, end=" ")
        num-=1
    print(end="  ")
    print("| ", end="")
    for j in range(N-1, i, -1):
        print(" ", end=" ")
    for k in range(-1,i):
        print(chr(ch), end=" ")
    print(end="  ")
    print("| ", end="")
    for j in range(N-1, i, -1):
        print(" ", end=" ")
    for k in range(-1,i):
        if i % 2 == 0:
            print(chr(ch), end=" ")
        else :
            print(num2, end=" ")
    print("  |", end=" ")
    num2-=1
    num=N
    ch+=1
    print()

print("---------------------------------------------------------")
ch = 65+N-1
num = 1
for i in range(N):
    print("| ", end="")
    for j in range(N, i, -1):
        print("#", end=" ")
    for k in range(-1, i):
        print(" ", end=" ")
    print("| ", end="")
    for j in range(N, i, -1):
        print(num, end=" ")
    for k in range(-1, i):
        print(" ", end=" ")
    print("| ", end="")
    for l in range(N, i, -1):
        print(chr(ch), end=" ")
    for k in range(-1, i):
        print(" ", end=" ")
    print("| ", end="")
    for m in range(N, i, -1):
        if i < N/2:
            print(num, end=" ")
        else :
            print(chr(ch), end=" ")
    for k in range(-1, i):
        print(" ", end=" ")
    print("|", end=" ")
    print()
    ch-=1
    num+=1

print("---------------------------------------------------------")
