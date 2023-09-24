a = 'Shilajit'  # Single Quoted String
b = "Shilajit"  # Double Qouted String
c = '''Shilajit'''  # Triple Quoted String

print(a, b, c)

# a[0]="a" This does not work
# String Index
print("**Using Positive Index**")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])

# String Negative Index
print("**Using Negative Index**")
print(a[-8])
print(a[-7])
print(a[-6])
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])

# String Slicing
print("**String Slicing**")
name = "Merry"
print(name[0:3])
print(name[1:3])
print(name[0:4])
print(name[2:4])
print(name[4:5])
print(name[4:4])  # This will print nothing
print(name[0:5])

# Advance Slicing
print("**Advance Slicing**")
print(name[0:])  # Same as name[0:5]
print(name[:5])  # Same as name[0:5]
print(name[-5:-2])
print(name[-5:5])  # Same as name[0:5]
print(name[-5:])  # Same as name[0:5] and same as name[-5:5]

print(name[:0])  # This will print nothing
print(name[-1:-5])  # This will print nothing

# Slicing with skip value
print("**Slicing with skip value**")
word = "Amazing"
print(word[1:6:2])  # Skipping 2-1=1 character from 1 to 5
print(word[0::3])  # Skipping 3-1=2 character from starting to end
# Skipping 1-1=0 character...so no character skip..Full string will be print
print(word[0::1])
print(word[2:6:4]) # Skipping 4-1=3 character from 2 to 5