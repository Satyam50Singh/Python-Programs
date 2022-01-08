# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def Pangram(s):
    temp = "".join(s.split(' '))
    s1 = sorted(list(set(temp.lower())))
    print("Yes, It's Pangrams") if len(
        s1) == 26 else print("No, It's not Pangrams")


s = "The quick brown fox jumps over the lazy dog"
Pangram(s)
