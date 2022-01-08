#WAP to print table from 1-10.

for i in range(1, 11):
    for j in range(1, 11):
        print(j ,'*', i ,"=", (i*j), end="\t")
    print("\n")
