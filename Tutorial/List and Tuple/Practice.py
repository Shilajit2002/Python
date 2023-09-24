# Question 1
f1=input("Enter 1st Fruit : ")
f2=input("Enter 2nd Fruit : ")
f3=input("Enter 3rd Fruit : ")
f4=input("Enter 4th Fruit : ")
f5=input("Enter 5th Fruit : ")
f6=input("Enter 6th Fruit : ")
f7=input("Enter 7th Fruit : ")

Fruit_list=[f1,f2,f3,f4,f5,f6,f7]
print(Fruit_list)
Fruit_list.sort()
print(Fruit_list)

# Question 2
m1 = int(input("Enter 1st Student Mark : "))
m2 = int(input("Enter 2nd Student Mark : "))
m3 = int(input("Enter 3rd Student Mark : "))
m4 = int(input("Enter 4th Student Mark : "))
m5 = int(input("Enter 5th Student Mark : "))
m6 = int(input("Enter 6th Student Mark : "))

Marks_list = [m1, m2, m3, m4, m5, m6]
print(Marks_list)
Marks_list.sort()
print(Marks_list)

# Question 3
list=[58,14,200,56,31]
sum1=list[0]+list[1]+list[2]+list[3]+list[4]
print(sum1)
print(sum(list))

# Question 5
tuple=(7,0,8,0,0,9)
print("0 is ",tuple.count(0)," times")
