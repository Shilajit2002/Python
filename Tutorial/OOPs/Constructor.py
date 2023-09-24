# Creating a Class
class Employee:
    # Constructor
    def __init__(self):
        print("Default Constructor")
        
# Creating Employee Class Object
rahul = Employee()

# Creating a Class
class Employee1:
    # Parameterized Constructor
    def __init__(self,name):
        self.name=name
        print(self.name)
        
# Creating Employee Class Object
jir = Employee1("Jit Ganguly")
