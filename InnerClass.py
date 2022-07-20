
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def display(self):
        print(self.name, self.rollno)
        self.lap.display()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        def display(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Navin', 2)
s2 = Student('Teja', 3)

s1.display()
s2.display()

lap1 = Student.Laptop()
lap2 = Student.Laptop()