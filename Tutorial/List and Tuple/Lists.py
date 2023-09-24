l = ["Apple", 17, 22.32, True, False, "Jit"]
print(l)

# List Index
print("**Using Positive Index**")
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])

# List Negative Index
print("\n**Using Negative Index**")
print(l[-6])
print(l[-5])
print(l[-4])
print(l[-3])
print(l[-2])
print(l[-1])

# List Slicing
print("\n**List Slicing**")
print(l[0:3])
print(l[1:3])
print(l[0:4])
print(l[2:4])
print(l[4:5])
print(l[4:4])  # This will print nothing
print(l[0:6])

# Advance Slicing
print("\n**Advance Slicing**")
print(l[0:])  # Same as l[0:6]
print(l[:6])  # Same as l[0:6]
print(l[-6:-2])
print(l[-6:6])  # Same as l[0:6]
print(l[-6:])  # Same as l[0:6] and same as l[-6:6]

print(l[:0])  # This will print empty list
print(l[-1:-5])  # This will print empty list

# Slicing with skip value
print("\n**Slicing with skip value**")
print(l[0:6:2])  # Skipping 2-1=1 element from 1 to 5
print(l[0::3])  # Skipping 3-1=2 element from starting to end
# Skipping 1-1=0 character...so no element skip..Full List will be print
print(l[0::1])
print(l[1:6:4])  # Skipping 4-1=3 element from 1 to 5

print("\n**Empty List**")
# Empty List
l1 = []
print(l1)

# List with 1 element
l2 = ["Jit"]
print(l2)

# Update list Value
print("\n**Update Some Value in List**")
l[0] = "Orange"
l[1] = 90
l[4] = None
print(l)  # This will update the main list

# Tuple in List
l4=[(1,1,5,8),(8,6,9,2)]
print(l4)
print(l4[0])
print(l4[1])
print(l4[0][2])
print(l4[1][1])