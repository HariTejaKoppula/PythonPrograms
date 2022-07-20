"""Method OverLoading"""
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s

s1 = Student(58, 69)
s2 = Student(69, 65)

print(s1.sum(16, 25, 9))

"""Method OverRiding"""
class A:
    def display(self):
        print("in A Display")
class B(A):
    def display(self):
        print("in B Display")


a1 = B()
a1.display()