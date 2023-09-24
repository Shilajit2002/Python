# Question1
print("------Question 1------")


class C2D_Vec:
    def __init__(self, i, j):
        self.iCap = i
        self.jCap = j

    def __str__(self):
        return f"{self.iCap}î + {self.jCap}ĵ"


class C3D_Vec(C2D_Vec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kCap = k

    def __str__(self):
        return f"{super().__str__()} + {self.kCap}k̂"


C2 = C2D_Vec(3, 4)
C3 = C3D_Vec(4, 5, 8)

print(C2)
print(C3)


# Question2
print("------Question 2------")


class Animal:
    def __init__(self):
        pass


class Pets(Animal):
    def __init__(self):
        pass


class Dog(Pets):
    def __init__(self):
        pass

    def bark(self):
        print("Bow Bow...")


D = Dog()
D.bark()

# Question3
print("------Question 3------")


class Employee:
    salary = 50000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, s):
        self.increment = s/self.salary


E = Employee()
print(E.salaryAfterIncrement)
E.salaryAfterIncrement = 100000
print(E.salary)
print(E.increment)

# Question4
print("------Question 4------")


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, c):
        return ComplexNumber(self.real+c.real, self.imaginary+c.imaginary)

    def __mul__(self, c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImg = self.real*c.imaginary+self.imaginary*c.real
        return ComplexNumber(mulReal, mulImg)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"


CN = ComplexNumber(3, 4)
CN1 = ComplexNumber(10, 15)
print(CN+CN1)
print(CN*CN1)

# Question5
print("------Question 5------")


class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)


v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1+v2)
print(v1*v2)
print(len(v1))
print(len(v2))

# Question6
print("------Question 6------")


class Vector1:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"


v1 = Vector1([1, 4, 6])
v2 = Vector1([1, 6, 9])
print(v1)
print(v2)
