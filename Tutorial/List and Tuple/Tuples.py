t = ("Apple", 17, 22.32, True, False, "Jit")
print(t)

# Tuple Index
print("**Using Positive Index**")
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t[5])

# Tuple Negative Index
print("\n**Using Negative Index**")
print(t[-6])
print(t[-5])
print(t[-4])
print(t[-3])
print(t[-2])
print(t[-1])

# Tuple Slicing
print("\n**Tuple Slicing**")
print(t[0:3])
print(t[1:3])
print(t[0:4])
print(t[2:4])
print(t[4:5])
print(t[4:4])  # This will print nothing
print(t[0:6])

# Advance Slicing
print("\n**Advance Slicing**")
print(t[0:])  # Same as t[0:6]
print(t[:6])  # Same as t[0:6]
print(t[-6:-2])
print(t[-6:6])  # Same as t[0:6]
print(t[-6:])  # Same as t[0:6] and same as t[-6:6]

print(t[:0])  # This will print empty Tuple
print(t[-1:-5])  # This will print empty Tuple

# Slicing with skip value
print("\n**Slicing with skip value**")
print(t[0:6:2])  # Skipping 2-1=1 element from 1 to 5
print(t[0::3])  # Skipping 3-1=2 element from starting to end
# Skipping 1-1=0 character...so no element skip..Full Tuple will be print
print(t[0::1])
print(t[1:6:4])  # Skipping 4-1=3 element from 1 to 5

print("\n**Empty Tuple**")
# Empty Tuple
t1 = ()
print(t1)

# Tuple with 1 element
t2 = ("Jit",)
print(t2)
t3 = ("Happy")
print(t3)  # This is wrong process for assign tuple with 1 element


# Update list Value
print("\n**Update Some Value in Tuple**")
''' You cannot direct chnage the value of tuple,it will show error
 t[0] = "Orange"  'tuple' object does not support item assignment
 At first convert list from tuple then update the value then convert tuple from list '''

t = list(t)

t[0] = "Orange"
t[1] = 90
t[4] = None

t = tuple(t)

print(t)  # This will update the main tuple

# List in Tuple
t4=([1,1,5,8],[8,6,9,2])
print(t4)
print(t4[0])
print(t4[1])
print(t4[0][2])
print(t4[1][1])
