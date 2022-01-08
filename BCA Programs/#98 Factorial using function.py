# Write a Python function to calculate the factorial of a number (a non- negative integer).
# The function accepts the number as argument

from functools import reduce


def Factorial(n):
    l = list(range(2, (n+1)))
    return reduce(lambda x, y: x*y, l)


print("Factorial :", Factorial(5))
