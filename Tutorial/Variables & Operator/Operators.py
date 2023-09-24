# Arithmetic Operators
x = 15
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x % y)
print(x//y)
print(x**y)

# Assignment Operators
x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)
x %= y
print(x)
x //= y
print(x)
x **= y
print(x)
x = 15
y = 2
x &= y
print(x)
x |= y
print(x)
x ^= y
print(x)
x >>= y
print(x)
x <<= y
print(x)

# Comparison Operators
x = 100
y = 200
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators
print(x and y)
print(x or y)
print(not(x and y))

# Identity Operators
print(x is y)
print(x is not y)

# Membership Operators
x = [1, 3]
y = [3]
print(x in y)
print(x not in y)

# Bitwise Operators
x = 12
y = 13
print(x & y)
print(x | y)
print(x ^ y)
print(~(x & y))
print(x << y)
print(x >> y)

# Conversion
print("**Decimal to Binary,Octal,Hexadecimal**")
print(bin(12))
print(oct(12))
print(hex(12))

print("**Binary,Octal,Hexadecimal to Decimal**")
print(0b1101)
print(0o10)
print(0xE)

print("**Binary to Octal and Octal to Binary**")
print(oct(0b1111))
print(bin(0o14))

print("**Binary to Hexadecimal and Hexadecimal to Binary**")
print(hex(0b1111))
print(bin(0xF))

print("**Octal to Hexadecimal and Hexadecimal to Octal**")
print(oct(0xA))
print(hex(0o20))