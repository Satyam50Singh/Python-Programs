# WAP that takes a list of words and return the length of longest word.

n = int(input("Enter the value of n :"))

list = []

for i in range(n):
    s = input("Word :")
    list.append(s)

maxLen = len(list[0])
maxWord = list[0]

for i in list:
    temp = len(i)
    if(temp>maxLen):
        maxLen = temp
        maxWord = i

print(list)
print("largest word is :", maxWord)
print("length of largest word is",maxLen)