t = (80, 25, 963, 248, 962, 10, 3, 25, 40, 75, 25)
t1 = ("Alexa", "Zina", "Jhon", "Yeak")
t2 = ("Apple", 17, 22.32, True, False, "Apple")

# 1.len()
print("Length of 1st Tuple = ", len(t))
print("Length of 2nd Tuple = ", len(t1))
print("Length of 3rd Tuple = ", len(t2))

# 2.count()
print("\n**Count Function**")
print(t.count(25))
print(t1.count("Zina"))
print(t2.count("Apple"))

# 3.sort()
print("\n**Sort Function**")
# Tuple have no sort function..at first convert tuple to list then apply sorting after that convert list to tuple
t=list(t)
t1=list(t1)
t.sort()  
t1.sort()
# l2.sort() This Will Error =>not supported between instances of 'int' and 'str'
t=tuple(t)
t1=tuple(t1)

print(t)
print(t1)

# 4.reverse()
print("\n**Reverse Function**")
t=list(t)
t1=list(t1)
t2=list(t2)

t.reverse() 
t1.reverse()  
t2.reverse() 

t=tuple(t)
t1=tuple(t1)
t2=tuple(t2)

print(t)
print(t1)
print(t2)

# 5.append()
print("\n**Append Function**")

t=list(t)
t1=list(t1)
t2=list(t2)

t.append(1000)  
t1.append("Shilajit")
t2.append("Orange")

t=tuple(t)
t1=tuple(t1)
t2=tuple(t2)

print(t)
print(t1)
print(t2)

# 6.insert()
print("\n**Insert Function**")

t=list(t)
t1=list(t1)
t2=list(t2)

t.insert(5, 500)
t1.insert(2, "Bob")
t2.insert(4, 50.37)

t=tuple(t)
t1=tuple(t1)
t2=tuple(t2)

print(t)
print(t1)
print(t2)

# 7.pop()
print("\n**Pop Function**")

t=list(t)
t1=list(t1)
t2=list(t2)

t.pop(3)
t1.pop(2) 
t2.pop(5)

t=tuple(t)
t1=tuple(t1)
t2=tuple(t2)

print(t)
print(t1)
print(t2)

# 8.remove()
print("\n**Remove Function**")

t=list(t)
t1=list(t1)
t2=list(t2)

t.remove(963) 
t1.remove("Zina") 
t2.remove(False) 

t=tuple(t)
t1=tuple(t1)
t2=tuple(t2)

print(t)
print(t1)
print(t2)

# 9.index()
print("\n**Index Function**")
print("Position of 25 is (First Occurence) ", t.index(25))

# 10.Tuple concatenation
print("\n**List Concatenation**")
print(t+t1+t2)

# 11.extend()
print("\n**Extend Function**")
a = ["BMW", "Lamborgini"]
b = (90, 54, 78)
c = {78, 69, "Happy"}

t=list(t)
t1=list(t1)
t2=list(t2)

t.extend(a)
t1.extend(b)
t2.extend(c)

t=tuple(t)
t1=tuple(t1)
t2=tuple(t2)

print(t)
print(t1)
print(t2)

# 12.copy()
print("\n**Copy Function**")

t=list(t)
x = t.copy()
x=tuple(x)

print(x)

# 13.clear()
print("\n**Clear Function**")
# Main Tuple will be Clear

t=list(t)
t1=list(t1)
t2=list(t2)

t.clear()
t1.clear()
t2.clear()

t=tuple(t)
t1=tuple(t1)
t2=tuple(t2)

print(t)
print(t1)
print(t2)

# 14.unpacking Tuple
print("\n**Unpacking Tuple**")
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print("\n")

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
print("\n")

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
print("\n")

# 15.multiply Tuple
print("\n**Multiply Tuple**")
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 4

print(mytuple)

