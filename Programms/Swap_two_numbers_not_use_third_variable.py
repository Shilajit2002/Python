# swap 2 numbers without 3rd variable

a=int(input("Enter 1st no. = "))
b=int(input("Enter 2nd no. = "))

a=a+b
b=a-b
a=a-b

print("1st value is = ",a)
print("2nd value is = ",b)