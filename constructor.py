
class Computer:

    def __init__(self):
        self.name = "Teja"
        self.age = 28

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 30
c2 = Computer()

if c1.compare(c2):
    print("They are Same")
else:
    print("They are Different")

print(c1.name)
print(c2.name)