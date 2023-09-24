# Question1
print("----Question1----")
num1 = int(input("Enter a number = "))
num2 = int(input("Enter a number = "))
num3 = int(input("Enter a number = "))
num4 = int(input("Enter a number = "))

if (num1 >= num2 and num1 >= num3 and num1 >= num4):
    print(num1, "is Greatest of Four Numbers")
elif (num2 >= num1 and num2 >= num3 and num2 >= num4):
    print(num2, "is Greatest of Four Numbers")
elif (num3 >= num1 and num3 >= num2 and num3 >= num4):
    print(num3, "is Greatest of Four Numbers")
elif (num4 >= num1 and num4 >= num2 and num4 >= num3):
    print(num4, "is Greatest of Four Numbers")
else:
    print(num1, num2, num3, num4)

# Question2
print("----Question2----")
Math = int(input("Enter your Math Marks = "))
Physics = int(input("Enter your Physics Marks = "))
Biology = int(input("Enter your Biology Marks = "))

total = (Math+Physics+Biology)/3

if (Math >= 33 and Physics >= 33 and Biology >= 33 and total >= 40):
    print("**You are Pass**")
else:
    print("`~`You are Fail`~`")

# Question3
print("----Question3----")
spamText = input("Enter Comment = ")

if ("make a lot of money" in spamText or "buy now" in spamText or "subscribe now" in spamText or "click this" in spamText):
    print("Spam!!!!!!!!!!")
else:
    print("Not Spam")

# Question4
print("----Question4----")
username = input("Enter your Username : ")
if (len(username) >= 10):
    print("Username Contains 10 Characters")
else:
    print("Username Contains less than 10 Characters")

# Question5
print("----Question5----")
nameList = ["Shilajit", "Jit", "Alex", "Bob", "Marry"]
name = input('Enter your name : ')

if (name in nameList):
    print("Name is present in the list")
else:
    print("Name is not presnent in the list")

# Question6
print("----Question6----")
marks = int(input("Enter Your Marks = "))
if (marks >= 90):
    print("Ex")
elif (marks >= 80):
    print("A")
elif (marks >= 70):
    print("B")
elif (marks >= 60):
    print("C")
elif (marks >= 50):
    print("D")
else:
    print("F")

# Question7
print("----Question7----")
post = input("Enter Your Post : ")

if (post.upper().find("HARRY") >= 0):
    print("Post is Talking About 'Harry'")
else:
    print("Post is Not Talking About 'Harry'")
