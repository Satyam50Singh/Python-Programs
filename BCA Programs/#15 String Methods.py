# String Methods part - I

str1 = "          Satyam         Singh       ##  "

# 1. strip()
print("strip() : ", str1.strip())

# 2. lstrip()
print("lstrip() : ", str1.lstrip())

# 3. rstrip()
print("rstrip() : ", str1.rstrip())

# 4. upper()
print("upper() : ", str1.upper())

# 5. lower()
print("lower() : ", str1.lower())

# 6. replace(old_char, new_char)
print("replace() : ", str1.replace(' ', 'a'))

# 7. swapcase()
print("swapcase() : ", str1.swapcase())

# 8. split()
print("\nsplit() : ", str1.split())
print("\nsplit('char') : ", str1.split('a'))
print("\nsplit('char', count) : ", str1.split('a', 1))
