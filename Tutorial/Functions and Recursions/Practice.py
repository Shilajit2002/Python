# Question1
print("----Question1----")


def greatest(num1, num2, num3):
    if (num1 >= num2 and num1 >= num3):
        return num1
    elif (num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3


num1 = int(input("Enter no1 = "))
num2 = int(input("Enter no2 = "))
num3 = int(input("Enter no3 = "))

print("Greatest Number is =", greatest(num1, num2, num3))

# Question2
print("----Question2----")


def cToF(celsius):
    return (celsius*1.8)+32


celsius = float(input("Enter Celcius = "))

print("Farenheit =", cToF(celsius), "°F")

# Question3
print("----Question3----")

print("Hello", end=" ")
print("How", end=" ")
print("are", end=" ")
print("you?")

# Question4
print("----Question4----")


def sumofN(num):
    if (num == 1):
        return 1
    else:
        return num + sumofN(num-1)


num = int(input("Enter Number = "))
print("Sum of first", num, "natural numbers =", sumofN(num))

# Question5
print("----Question5----")


def pattern(row):
    for i in range(row, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print("")


row = int(input("Enter Row = "))
pattern(row)

# Question6
print("----Question6----")


def inchTocm(inch):
    return inch*2.54


inch = int(input("Enter Inches = "))
print("Centimeter =", inchTocm(inch))

# Question7
print("----Question7----")


def rem(lis, word):
    lis.remove(word)
    for i in range(len(lis)):
        lis.insert(i, lis.pop(i).strip())
    return lis


lis = ["Hello", "          Jit          ", "         Welcome       ", "Thanks"]
print(rem(lis, "Hello"))

# Question7
print("----Question7----")


def mul(num):
    for i in range(11):
        print(num, "X", i, "=", num*i)


mul(10)
