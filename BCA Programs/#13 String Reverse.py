#WAP to get a string from user and print
# 1. Length
# 2. In reverse sequence

str = input("Enter a string :")

print("\nString is :",str)

print("\nString length is (Using len method) :",len(str))

len=0
for i in str:
    len+=1

print("\nString length is (Without Using len method) :",len)


print("\nString in reverse (Without Using method) : ", end="")

for i in range(-1,-(len+1), -1):
    print(str[i], end="")

print("\n\nString in reverse (Using slcing) : ", str[::-1])
