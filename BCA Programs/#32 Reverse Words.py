# WAP to print reverse words in a string.

str = input("Enter a string :")
list = str.split()
print("\nWords \n", list)
print("\nWords in reverse Sequence \n")
for i in reversed(list):
    print(i, sep="  ", end="")

print("\nWords in reverse & also in reverse Sequence\n")
for i in reversed(list):
    for j in reversed(i):
        print(j, end=" ")    
    print(end=" ")