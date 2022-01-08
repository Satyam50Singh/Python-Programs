# Program to print a pattern using class and object.

class Pattern:  # class in python
    rows = 5  # member variables

    def __init__(self, n):  # constructor
        self.rows = n

    def printPattern(self):  # member functions
        for i in range(self.rows):
            for j in range(0, i):
                print("*", end=" ")
            print()


obj = Pattern(6)  # creating objects

obj.printPattern()  # function calling
