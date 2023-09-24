# Question1
print("---Question 1---")

dictionary = {
    "Pankha": "Fan",
    "Mombatti": "Candle",
    "Pani": "Water"
}

print("Your Options Are : ", dictionary.keys())
a=input("Enter the Hindi Word : ")
print("The Meaning of the "+a+" is : ",dictionary.get(a))

# Question2
print("---Question 2---")

num1=int(input("Enter Number 1 = "))
num2=int(input("Enter Number 2 = "))
num3=int(input("Enter Number 3 = "))
num4=int(input("Enter Number 4 = "))
num5=int(input("Enter Number 5 = "))
num6=int(input("Enter Number 6 = "))
num7=int(input("Enter Number 7 = "))
num8=int(input("Enter Number 8 = "))

unique={num1,num2,num3,num4,num5,num6,num7,num8}

print(unique)

# Question3
print("---Question 3---")

l={18,"18"}
print(l)

# Question4
print("---Question 4---")

s=set();
s.add(20);
s.add(20.0)
s.add("20")
print(s)
print("Length of S set is = ",len(s))

# Question5
print("---Question 5---")

S={}
print(type(S))


# Question6
print("---Question 6---")
Lang = {}

x = input("Enter your name : ")
y = input("Enter your favourite language : ")

Lang.update({
    x: y
})

x = input("Enter your name : ")
y = input("Enter your favourite language : ")

Lang.update({
    x: y
})

x = input("Enter your name : ")
y = input("Enter your favourite language : ")

Lang.update({
    x: y
})

x = input("Enter your name : ")
y = input("Enter your favourite language : ")

Lang.update({
    x: y
})

print(Lang)

# Question7
# print("---Question 7---")
# Key Must be Unique so if there same key is present then recent key is updated and previous one deleted

# Question8
# print("---Question 8---")
# Nothing will happen if there are same value.Because value is not need to be unique

# Question 9
# print("---Question 8---")
# No because set does not contain any list
