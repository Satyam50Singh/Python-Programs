# Write a Python function to check whether a number is perfect or not. Note: In number theory, a perfect number is a positive integer that is
# equal to the sum of its proper positive divisors, that is, the sum of its
# positive divisors excluding the number itself (also known as its aliquot
# sum). Equivalently, a perfect number is a number that is half the sum
# of all of its positive divisors (including itself).
#
# Example : The first perfect number is 6, because 1, 2, and 3 are its
# proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number
# 6 is equal to half the sum of all its positive divisors: (1 + 2 + 3 + 6) /
# 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is
# followed by the perfect numbers 496 and 8128


def checkPerfectNumber(n):
    temp = n
    rev = 0
    i = 1

    print("Factors :-")
    while i < n:
        if temp % i == 0:
            rev += i
            print(rev, end="  ")
        i += 1

    print("\nYes,n is perfect no.") if rev == n else print(
        "\nNo,n is not perfect no.")


n = 28
checkPerfectNumber(n)
