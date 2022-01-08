# create an class
class Employee:
    __empId = 101  # Private Variable
    _college = "SGRR UNIVERSITY"  # Protected Variable
    name = "Satyam Singh"  # Public variable

    # non-parameterised constructor
    def __init__(self):
        print("Non - Parameterised Constructor.")

    # parameterised constructor
    def __init__(self, age):
        self.age = age

    # destructor
    def __del__(self):
        print("Destructor")

    # methods
    def display(self):
        print(self.__empId, self.name, self.age)


# create class object
E1 = Employee(21)
E2 = Employee(62)

# function invocation
E1.display()
E2.display()

# delete an object
del E1
