# Program to print an pattern
#     #
#    *#*
#   **#**
#  ***#***
# ****#****
N = int(input("ENTER VALUE OF N:"))

for i in range(N):
    for j in range(N-1, i, -1):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print("#", end="")
    for k in range(i):
        print("*", end="")
    print()
