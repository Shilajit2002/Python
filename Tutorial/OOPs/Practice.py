# Question 1
print("-------- Question 1 --------")


class Programmer:
    company = "Microsoft"

    def __init__(self, name, sp):
        self.name = name
        self.sp = sp


P1 = Programmer("Alex", "Java")
print("Name :", P1.name)
print("Specialist :", P1.sp)

P2 = Programmer("John", "Python")
print("Name :", P2.name)
print("Specialist :", P2.sp)

P3 = Programmer("Mark", "React")
print("Name :", P3.name)
print("Specialist :", P3.sp)


# Question 2
print("-------- Question 2 --------")


class Calculator:
    def __init__(self, n):
        self.n = n

    def Square(self):
        print(f"Square of {self.n} is = {self.n**2}")

    def Cube(self):
        print(f"Cube of {self.n} is = {self.n**3}")

    def squareRoot(self):
        print(f"Square Root of {self.n} is = {self.n**0.5}")

    @staticmethod
    def greet():
        print("Hello")


C1 = Calculator(4)
C1.Square()
C1.Cube()
C1.squareRoot()

C2 = Calculator(457846)
C2.Square()
C2.Cube()
C2.squareRoot()

# Question 3
print("-------- Question 3 --------")


class Check:
    a = 1


ob = Check()
ob.a = 0
print(Check.a)
print(ob.a)
# Ans => Its Not Change

# Question 4
print("-------- Question 4 --------")

user = Calculator(85)
user.greet()

# Question 5
print("-------- Question 5 --------")


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if (self.seats > 0):
            print(
                f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full!!")


intercity = Train("Intercity Express : 14015", 90, 2)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()

kanchan = Train("KanchanJangha Express : 14015", 450, 20)
kanchan.getStatus()
kanchan.fareInfo()
kanchan.bookTicket()
kanchan.bookTicket()
kanchan.bookTicket()
kanchan.getStatus()

# Question 6
print("-------- Question 6 --------")


class Change:
    def Greet(slf):
        print("Hello", slf.name)


ch = Change()
ch.name = "Jit"
ch.Greet()

# Ans => Yes we can change self parameter by using any name like slf,abcd whatever we want.That doesnot effect on code.
