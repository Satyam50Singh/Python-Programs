# WAP to find the first appearacnce of the substring 'not' and 'poor' from a given string.
# if 'not' follows the 'poor', replaces the whole 'not'...'poor' substring with 'good'.return the resulting string.

# string - 'the lyrics is not that poor'
# o/p - 'the lyrics is good'

str = input("Enter a string :")

i1 = str.find('not')
i2 = str.find('poor')


if(i1 == -1 or i2 == -1):
    print(str)
else :
    if(i1<i2):
        temp=""
        for i in range(i1): 
            temp+=str[i]
        temp+="good"
        for i in range((i2+4), len(str)): 
            temp+=str[i]
        print(temp)
