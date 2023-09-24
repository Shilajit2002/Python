l = [80, 25, 963, 248, 962, 10, 3, 25, 40, 75, 25]
l1 = ["Alexa", "Zina", "Jhon", "Yeak"]
l2 = ["Apple", 17, 22.32, True, False, "Apple"]

# 1.len()
print("Length of 1st list = ", len(l))
print("Length of 2nd list = ", len(l1))
print("Length of 3rd list = ", len(l2))

# 2.count()
print("\n**Count Function**")
print(l.count(25))
print(l1.count("Zina"))
print(l2.count("Apple"))

# 3.sort()
print("\n**Sort Function**")
l.sort()  # Sort the main list
l1.sort()  # Sort the main list
# l2.sort() This Will Error =>not supported between instances of 'int' and 'str'
print(l)
print(l1)
# print(l2) Error

# 4.reverse()
print("\n**Reverse Function**")
l.reverse()  # Reverse the main list
l1.reverse()  # Reverse the main list
l2.reverse()  # Reverse the main list
print(l)
print(l1)
print(l2)

# 5.append()
print("\n**Append Function**")
l.append(1000)  # Adds 1000 at the end of the list and update the main list
# Adds Shilajit at the end of the list and update the main list
l1.append("Shilajit")
# Adds Orange at the end of the list and update the main list
l2.append("Orange")
print(l)
print(l1)
print(l2)

# 6.insert()
print("\n**Insert Function**")
l.insert(5, 500)  # Adds 500 at index 5 of the list and update the main list
l1.insert(2, "Bob")  # Adds Bob at index 2 of the list and update the main list
# Adds 50.37 at index 4 of the list and update the main list
l2.insert(4, 50.37)
print(l)
print(l1)
print(l2)

# 7.pop()
print("\n**Pop Function**")
l.pop(3)  # Delete Element at index 3 in the list and update the main list
l1.pop(2)  # Delete Element at index 2 in the list and update the main list
l2.pop(5)  # Delete Element at index 5 in the list and update the main list
print(l)
print(l1)
print(l2)

# 8.remove()
print("\n**Remove Function**")
l.remove(963)  # Delete Element 963 in the list and update the main list
l1.remove("Zina")  # Delete Element Zina in the list and update the main list
l2.remove(False)  # Delete Element False in the list and update the main list
print(l)
print(l1)
print(l2)

# 9.index()
print("\n**Index Function**")
print("Position of 25 is (First Occurence) ", l.index(25))

# 10.list concatenation
print("\n**List Concatenation**")
print(l+l1+l2)

# 11.extend()
# The extend() method adds the specified list elements (or any iterable Eg: set, tuple, etc.) to the end of the current list and update the main list
print("\n**Extend Function**")
a = ["BMW", "Lamborgini"]
b = (90, 54, 78)
c = {78, 69, "Happy"}

l.extend(a)
l1.extend(b)
l2.extend(c)
print(l)
print(l1)
print(l2)

# 12.copy()
print("\n**Copy Function**")
x = l.copy()
print(x)

# 13.clear()
print("\n**Clear Function**")
# Main List will be Clear
l.clear()
l1.clear()
l2.clear()
print(l)
print(l1)
print(l2)

# 14.unpacking list
print("\n**Unpacking List**")
fruits = ["apple", "banana", "cherry"]

[green, yellow, red] = fruits

print(green)
print(yellow)
print(red)
print("\n")

fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]

[green, yellow, *red] = fruits

print(green)
print(yellow)
print(red)
print("\n")

fruits = ["apple", "mango", "papaya", "pineapple", "cherry"]

[green, *tropic, red] = fruits

print(green)
print(tropic)
print(red)
print("\n")

# 15.multiply list
print("\n**Multiply List**")
fruits = ["apple", "banana", "cherry"]

print(fruits * 4)
