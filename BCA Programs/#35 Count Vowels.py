# WAP to count and display the vowels of a given text.

str = input("Enter an string :")

vowels = ['a', 'i', 'o', 'u', 'e', 'A', 'E', 'O', 'I', 'U']
count=0
print("Vowels :", end="")
for i in str:
    if i in vowels:
        count +=1
        print(i, sep=",", end=" ")

print("\nNumber of vowels :",count)