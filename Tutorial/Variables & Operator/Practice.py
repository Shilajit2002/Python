# Add Two Numbers
s = float(input("Enter a no. = "))
g = float(input("Enter a no. = "))

print("Sum of two no. is = ", s+g)

# Find Remainder
remain = int(input("Enter a no. = "))
print("The remainder of this no after diving by 2 is = ", remain % 2)

# Find Type of a Variable
var = input("Enter any thing : ")
print("The type of this is : ", type(var))  # This type is always string

# Comparison
a = 34
b = 80
print("a is greater than b : ", a > b)
print("a is less than b : ", a < b)

# Find Average
one = float(input("Enter a no. = "))
two = float(input("Enter a no. = "))
print("Average is = ", (one+two)/2)

# Find square of a no.
sq = float(input("Enter a no. = "))
# First Process => using multiplication => sq multiply by sq
print("Square of the no. is = ", sq*sq)
# Second Process => using exponential => sq to the power 2
print("Square of the no. is = ", sq**2)
