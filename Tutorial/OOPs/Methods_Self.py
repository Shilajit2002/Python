# Creating a Class
class Employee:
    # Methods
    # Self refers to the instance of the class
    def Greet(self):
        print(f"Hello {self.name} !! Welcome")
        
# Creating Employee Class Object
rahul = Employee()

rahul.name="Rahul Roy"
rahul.Greet()
