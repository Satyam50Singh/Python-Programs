# WAP thats accept a commas separated sequence of words as input and prints the unique word in sort order.
# str - 'red, white, black, red, green, black'
# o/p - black, green, red, white

str = input("Enter a string :")

colors = str.split(', ')

list = []

for i in colors :
    if i not in list :
        list.append(i)

list.sort()
print(list)
