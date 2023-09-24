class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # Without Using Class Method
    def changeSalary1(self, sal):
        # This will actually change the Class Salary Value
        self.__class__.salary = sal

    # With Using Class Method
    @classmethod
    # This will actually change the Class Salary Value
    def changeSalary2(cls, sal):
        cls.salary = sal


e = Employee()
print(e.salary)
print(Employee.salary)
e.changeSalary1(455)
print(e.salary)
print(Employee.salary)
e.changeSalary1(5000)
print(e.salary)
print(Employee.salary)
