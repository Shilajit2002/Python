class Student:
    # Instance Variables
    college = "CIEM"

    # Constructor
    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.dept = dept

    # Getter Name Module
    def getName(self):
        return self.name

    # Getter Roll Module
    def getRoll(self):
        return self.roll

    # Getter Dept Module
    def getDept(self):
        return self.dept

    # Setter Name Module
    def setName(self, name):
        self.name = name

    # Setter Roll Module
    def setRoll(self, roll):
        self.roll = roll

    # Setter Dept Module
    def setDept(self, dept):
        self.dept = dept

    @staticmethod
    def greet():
        print("Welcome !!")


x = Student("Shilajit Acharjee", 16500120028, "CSE")
x.greet()
print("College : ", x.college)
print("Name :", x.getName())
print("Roll :", x.getRoll())
print("Dept :", x.getDept())

print("---------------------------")

x.greet()
x.setName("John Abraham")
x.setRoll(16500140024)
x.setDept("ECE")
print("College : ", x.college)
print("Name :", x.getName())
print("Roll :", x.getRoll())
print("Dept :", x.getDept())
