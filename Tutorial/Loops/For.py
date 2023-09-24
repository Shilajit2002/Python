# List Iteration
l = [1, 7, 8]
for item in l:
    print(item)

print("----------------------")

# Tuple Iteration
t = (1, 2, 4, 6)
for item in t:
    print(item)

print("----------------------")

# Dictionary Iteration
d = {
    "Hello": 3,
    "world": True,
    5: "Welcome"
}
for item in d:
    print("Key =", item, ", Value =", d[item])

print("----------------------")

# Set Iteration
s = {1, 2, 4, 5, 6, 7, 8}
for item in s:
    print(item)

print("----------------------")

for i in range(10):
    print(i)

print("----------------------")

for i in range(1, 10):
    print(i)

print("----------------------")

for i in range(1, 10, 2):
    print(i)

print("----------------------")

# For Loop With Else
for item in l:
    print(item)
else:
    print("Done")
