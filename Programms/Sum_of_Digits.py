# three digit number whose sum of the digits is to be calculated

n = int(input("Enter a 3 digit number = "))
s =0
while n>0 :
    m = n%10
    n = n//10
    s=s+m
print("Sum of 3 digits are = ",s)