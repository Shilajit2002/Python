class Employee:
    salary = 5000
    salaryBonus = 500

    # Getter Method
    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

    # Setter Method
    @totalSalary.setter
    def totalSalary(self, val):
        self.salary = val-self.salaryBonus


E = Employee()
# Call as an Attribute not a function
print(E.totalSalary)
# Set as an Attribute not a function
E.totalSalary = 7890
print(E.salary)
print(E.salaryBonus)
