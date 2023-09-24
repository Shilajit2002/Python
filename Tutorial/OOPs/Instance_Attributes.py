# Creating a Class
class Employee:
    # Instance Variable
    company = "Google"
    salary = 10000


# Creating Employee Class Object
rahul = Employee()

print("Rahul Company is :", rahul.company)
print("Rahul Salary is :", rahul.salary)

# Creating Another Employee Classs Object
jit = Employee()

# Changing Instance Attributes
jit.company = "You Tube"
jit.salary = 1000000

print("Jit Company is :", jit.company)
print("Rahul Salary is :", jit.salary)
