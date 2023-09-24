a = 71  # Identifies a as class integer
b = 88.44  # Identifies b as class float
c = "Shilajit Acharjee"  # Identifies c as class string
d = True
e = False  # Identifies d and e as class Boolean
f = None  # Indentifies f as class None
g = 1j  # Identifies g as class Complex

# Type of datatypes
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

# Type casting
integer = 1234
float1 = 12.28
string = "Welcome Boss"
string2 = "1254"
Bool = True
none = None
Complex = 1j

print(int(float1), int(string2), int(Bool))  # Conversion Integer
print(float(integer), float(string2), float(
    Bool))  # Conversion Float
print(str(float1), str(integer), str(Bool), str(Complex))  # Conversion String
print(bool(float1), bool(string2), bool(integer),
      bool(none), bool(string), bool(Complex))  # Conversion Bool
print(complex(float1), complex(string2), complex(integer))  # Conversion Complex
