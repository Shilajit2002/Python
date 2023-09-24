# Creating a Class
class Employee:
    # Instance Variable
    company = "Google"


# Creating Employee Class Object
rahul = Employee()

print("Rahul Company is :", rahul.company)

# Changing Class Attribute
Employee.company = "YouTube"

# Creating Another Employee Classs Object
jit = Employee()

print("Jit Company is :", jit.company)

print("Rahul Company is :", rahul.company)
