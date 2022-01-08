# String Methods part - II

str = "    HI i am satya\n Singh   72 zh @"

# 9. splitlines()
print("\nsplitlines() : ", str.splitlines());
print("\nsplitlines() : ", str.splitlines(True));

# 10. join()

str2 = ["Namaste"," Ji"," hahaha"," 2019"]
print("\njoin() : ", '#'.join(str2))

# 11. capitalize()
str3 = "am satya Singh   72 zh @"
print("\ncapitalize() : ", str3.capitalize())

# 12. center()
str4 = "Apple"
print("\ncenter() : ", str4.center(40, '#'))
print("\ncenter() : ", str4.center(40))

# 13. ljust()
print("\nljust() : ", str4.ljust(40, '#'))
print("\nljust() : ", str4.ljust(40))

# 14. rjust()
print("\nrjust() : ", str4.rjust(40, '#'))
print("\nrjust() : ", str4.rjust(40))

# 15. count()
print("\ncount() : ", str4.count('p'))

# 16. startswith()
print("\nstr4.startswith('a') : ", str4.startswith('a'))

# 17. endswith()
print("\nstr4.endswith('e') : ", str4.endswith('e'))

