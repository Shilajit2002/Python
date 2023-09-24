# input 599321 output will be 5+9+9+3+2+1

n = input("Enter a 3 digit number = ")
sum =0
for i in n:
    sum=sum+int(i)
print("Sum of all digits are = ",sum)