a = 24
if (a > 90):
    print(a, " is greater than 90")
elif (a < 40):
    print(a, " is less than 40")
else:
    print("None")

print("--------------------------")

# Quick Quiz
age = int(input("Enter your age = "))
if (age >= 18):
    print("You are Adult")
else:
    print("You are not adult")

print("--------------------------")

# Logical Operators
if (1 == 1 and 2 == 3):
    print("Correct")
else:
    print("Wrong")

print("--------------------------")

if (1 == 1 or 2 == 3):
    print("Correct")
else:
    print("Wrong")

print("--------------------------")

if (not False):
    print("True")

print("--------------------------")

# Is Operator
x = None
if (x is None):
    print(x)
else:
    print("Not None")

print("--------------------------")

# In Operator
l = [1, 2, 3, 4]
if (3 in l):
    print(("3 is Present in the list"))
    print(l)
