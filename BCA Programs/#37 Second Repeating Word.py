# WAP to find the second most repeating word in a given string.

str = "Today is sunday yesterday was also sunday and tomorrow will be also sunday"

List = str.lower().split(" ")

words = list(set(List))
cList = []

for i in words:
    cList.append(List.count(i))

size = len(cList)

for i in range(size):
    for j in range((size-i-1)):
        if cList[j] < cList[j+1]:
            temp = cList[j]
            temp2 = words[j]
            cList[j] = cList[j+1]
            words[j] = words[j+1]
            cList[j+1] = temp
            words[j+1] = temp2

print("\nOutput\n")
print("All Comman Words :",words)
print("Frequency of all comman words :",cList)

print("Second Most Repeating Character is:", words[1])