# Single Inheritance

# base class
class Person:
    def role(self):
        print("Person Class")


# child class
class Student (Person):
    def sRole(self):
        print("Role : - Student")


class Teacher(Person):
    def tRole(self):
        print("Role : - Teacher")


S1 = Student()
S1.sRole()
S1.role()

T1 = Teacher()
T1.tRole()
