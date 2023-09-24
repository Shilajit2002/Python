# Question1
print("----Question1----")
mul = int(input("Enter a Number = "))
print("Multiplication Table of", mul, "is : ")
for i in range(1, 11):
    print(mul, "X", i, "=", mul*i)

# Question2
print("----Question2----")
l1 = ["Harry", "Saham", "Sachin", "Rahul"]
for item in l1:
    if (item.startswith("S")):
        print("Hello", item, ", Welcome to Shark Tank.")

# Question3
print("----Question3----")
mul = int(input("Enter a Number = "))
print("Multiplication Table of", mul, "is : ")
i = 1
while (i <= 10):
    print(mul, "X", i, "=", mul*i)
    i = i+1

# Question4
print("----Question4----")
n = int(input("Enter a Number = "))
m = (int)((n)**(1/2))
flag = True

for i in range(2, m+1):
    if (n % i == 0):
        flag = False
        break

if (flag):
    print(n, "is a Prime Number")
else:
    print(n, "is not a Prime Number")

# Question5
print("----Question5----")
num = int(input("Enter a Number = "))
i = 0
sum = 0
while (i <= num):
    sum += i
    i = i+1
print("Sum of first", num, "natural number =", sum)

# Question6
print("----Question6----")
numFac = int(input("Enter a number for find factorial = "))
fact = 1
for i in range(1, numFac+1):
    fact *= i
print(numFac, "Factorial is =", fact)

# # Question7
print("----Question7----")
row = int(input("Enter row = "))
for i in range(1, row+1):
    for space in range(1, (row-i)+1):
        print("  ", end="")
    for j in range(1, (2*i-1)+1):
        print("* ", end="")
    print("")

# Question8
print("----Question8----")
for i in range(0, row):
    for j in range(0, i+1):
        print("* ", end="")
    print("")

# Question9
print("----Question9----")
for i in range(0, row):
    if (i % 2 == 0):
        for j in range(0, row):
            print("* ", end="")
        print("")
    else:
        print("* ", end="")
        for space in range(0, row-2):
            print("  ", end="")
        print("*")

# Question10
print("----Question10----")
mul = int(input("Enter a Number = "))
print("Multiplication Table of", mul, "in reverse order : ")
for i in range(10, 0, -1):
    print(mul, "X", i, "=", mul*i)
