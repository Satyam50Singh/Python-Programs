# WAP to capitalize first and last word .

str = input("Enter an string :")

str = str.title()

result = ""

for i in str.split():
    result += i[:-1] + i[-1].upper() + " "

print(result)
