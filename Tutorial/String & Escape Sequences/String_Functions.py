a = "Twinkle, twinkle, little star"

# 1.len()
print("Length is :", len(a))

# 2.endswith()
print('** Ends with Function **')
print(a.endswith("r"))
print(a.endswith("star"))
print(a.endswith("o"))

# 3.startswith()
print('** Starts with Function **')
print(a.startswith("T"))
print(a.startswith("Twinkle"))
print(a.startswith("t"))

# 4.count()
print("**Count Function**")
print(a.count("i"))
print(a.count("winkle"))
print(a.count("o"))

# 5.capitalize()
b = "hello"
print("**Capitalize Function**")
print(b.capitalize())

# 6.upper()
print("**Upper function**")
c = a.upper()
print(c)

# 7.isupper()
print("**IsUpper function**")
print(c.isupper())
print(a.isupper())

# 8.lower()
print("**Lower function**")
d = c.lower()
print(d)

# 9.islower()
print("**IsLower function**")
print(d.islower())
print(c.islower())

# 10.title()
print("**Title function**")
e = a.title()
print(e)

# 11.istitle()
print("**IsTitle function**")
print(e.istitle())
print(a.istitle())

# 12.find()
print("**Find function**")
print(a.find("winkle"))
print(a.find("t"))
print(a.find("hello"))

# 13.rfind()
print("**RFind function**")
print(a.rfind("winkle"))
print(a.rfind("t"))
print(a.rfind("hello"))

# 14.index()
print("**Index function**")
print(a.index("winkle"))
print(a.index("t"))
# print(a.index("hello"))  This will get error

# 15.rindex()
print("**RIndex function**")
print(a.rindex("winkle"))
print(a.rindex("t"))
# print(a.rindex("hello")) This will get error

# 16.replace()
print("**Replace function**")
print(a.replace("star", "moon"))
print(a.replace("t", "b"))

# 17.maketrans() and translate()
print("**Maketrans and translate function**")
x = "star"
y = "moon"
z = "i"
maketrans1 = a.maketrans(x, y)
print(a.translate(maketrans1))
maketrans2 = a.maketrans(x, y, z)
print(a.translate(maketrans2))

# 18.strip()
print("**Strip function**")
strip1 = "                   Hello                   "
print(strip1.strip())
strip2 = ",,,,,rrttgg.....banana....rrr"
print(strip2.strip(",.grt"))

# 19.lstrip()
print("**LStrip function**")
lstrip1 = "                   Hello                   "
print(lstrip1.lstrip(), "Merry")

# 20.rstrip()
print("**RStrip function**")
rstrip1 = "                   Hello                   "
print(rstrip1.rstrip(), "Merry")

# 21.split()
print("**Split function**")
print(a.split(","))
print(a.split(" "))
print(a.split(", "))

# 22.rsplit()
print("**RSplit function**")
print(a.rsplit(","))
print(a.rsplit(",", 1))

# 23.concatenation()
print("**String Concatenation**")
print(a+" "+"and nice moon")

# 24.format()
print("**Format function**")
Format = "I am {}"
print(Format.format("19"))

# 25.casefold()
print("**Casefold function**")
print(c.casefold())

# 26.center()
print("**Center function")
print(a.center(50))
print(a.center(50, "*"))

# 27.ljust()
print("**LJust function**")
print(a.ljust(50))
print(a.ljust(50, "*"))

# 28.rjust()
print("**LJust function**")
print(a.rjust(50))
print(a.rjust(50, "*"))

# 29.encode()
print("**Encode function**")
txt = "My name is Ståle"
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
# print(txt.encode(encoding="ascii",errors="strict")) This will error
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))

# 30.expandtabs()
print("**Expandtabs function**")
tabs = "H\tE\tL\tL\tO"
print(tabs.expandtabs())
print(tabs.expandtabs(4))
print(tabs.expandtabs(8))
print(tabs.expandtabs(16))
print(tabs.expandtabs(20))
print(tabs.expandtabs(30))

# 31.isalnum()
print("**IsAlnum function**")
alphanumeric = "CSE028"
print(alphanumeric.isalnum())
alphanumeric1 = "CSE028_345_!$#%^& *64 "
print(alphanumeric1.isalnum())

# 32.isalpha()
print("**IsAlpha function**")
alpha = "CsE"
print(alpha.isalpha())
print(alphanumeric1.isalpha())

# 33.isdecimal()
print("**IsDecimal function**")
dem = "\u0030"  # unicode for 0
dem1 = "\u0047"  # unicode for G
print(dem.isdecimal())
print(dem1.isdecimal())

# 34.isdigit()
print("**IsDigit function**")
dem = "16500120028"
dem1 = "\u0030"  # unicode for 0
dem2 = "\u00B2"  # unicode for ²
dem3 = "CSE028"
print(dem.isdigit())
print(dem1.isdigit())
print(dem2.isdigit())
print(dem3.isdigit())

# 35.isidentifier()
print("**IsIdentifier function**")
iden = "CSE_028"
iden1 = "78_oi$ui&*"
iden2 = "12Hyu"
print(iden.isidentifier())
print(iden1.isidentifier())
print(iden2.isidentifier())

# 36.isnumeric()
print("**IsNumeric function**")
dem = "16500120028"
dem1 = "\u0030"  # unicode for 0
dem2 = "\u00B2"  # unicode for ²
dem3 = "10km2"
dem4 = "-1"
dem5 = "1.5"
print(dem.isdigit())
print(dem1.isdigit())
print(dem2.isdigit())
print(dem3.isdigit())
print(dem4.isdigit())
print(dem5.isdigit())

# 37.isprintable()
print("**IsPrintable function**")
txt = "Hello! Are you #1?"
txt1 = "Hello! \nAre \tyou #1?"
print(txt.isprintable())
print(txt1.isprintable())

# 38.isspace()
print("**IsSpace function**")
space = " "
spcae1 = "               "
space2 = "      5        "
print(space.isspace())
print(spcae1.isspace())
print(space2.isspace())

# 39.partition()
print("**Partition function**")
parti = "Jhon..`~`.Hello you are most welcome, Hello!"
print(parti.partition("Hello"))

# 40.rpartition()
print("**RPartition function**")
parti = "Jhon..`~`.Hello you are most welcome, Hello!"
print(parti.rpartition("Hello"))

# 41.swapcase()
print("**Swapcase function**")
swap = "HellO You Are Most WelcomE"
print(swap.swapcase())

# 42.splitlines()
print("**Splilines function**")
txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines())
print(txt.splitlines(True))

# 43.zfill()
print("**Zfill function**")
a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10))
# This will not work because the length is lass than the actual string length
print(b.zfill(10))
print(c.zfill(10))
