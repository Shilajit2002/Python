import os

# Question1
print("---------Question1---------")
with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Poem.txt") as f:
    poem = f.read()

poem = poem.upper()
if "TWINKLE" in poem:
    print("Twinkle is Present in the Poem.txt")
else:
    print("Twinkle is Not Present in the Poem.txt")

# Question2
print("---------Question2---------")
s = int(input("Enter your game score = "))


def game(s):
    return s


with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Hiscore.txt") as fh:
    score = fh.read()

if (score == ""):
    with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Hiscore.txt", "w") as fh:
        fh.write(str(game(s)))
    print("Your Score is Added....Check Hiscore.txt")
elif (int(score) < game(s)):
    with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Hiscore.txt", "w") as fh:
        fh.write(str(game(s)))
    print("Your Score is Added....Check Hiscore.txt")
else:
    print("Your Score is low....not added")

# Question3
print("---------Question3---------")
for i in range(2, 21):
    with open(f"E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\MultiplicationTable\\MulTable{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i*j}\n")
print("Created Multiplication Table")

# Question4
print("---------Question4---------")
with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Donkey.txt", "r") as f:
    content = f.read()

if "donkey" in content.lower():
    content = content.lower().replace("donkey", "$#@%^##")

with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Donkey.txt", "w") as f:
    f.write(content)

print("Updated")

# Question5
print("---------Question5---------")
l = ["donkey", "stupid", "blusttered"]

with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Donkey.txt", "r") as f:
    content = f.read()
    for item in l:
        if item in content.lower():
            content = content.lower().replace(item, "$#@%^##")

with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Donkey.txt", "w") as f:
    f.write(content)

print("Updated")

# Question6
print("---------Question6---------")
with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Log.txt", "r") as f:
    log = f.read()

if "python" in log.lower():
    print("Python is Present in the List")
else:
    print("Python is not present in the list")

# Question7
print("---------Question7---------")
count = 1
f = open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Log.txt", "r")
log = f.readline()

while log:
    if "python" in log.lower():
        print("Python is Present in Line No. =", count)
    log = f.readline()
    count += 1
f.close()

# Question8
print("---------Question8---------")
with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Text.txt", "r") as f:
    copy = f.read()

with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Copy.txt", "w") as f:
    f.write(copy)

os.remove("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Text.txt")
print("Copied")

# Question9
print("---------Question9---------")

file1 = "E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Copy.txt"
file2 = "E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Match.txt"

with open(file1, "r") as f:
    f1 = f.read()
with open(file2, "r") as f:
    f2 = f.read()

if (f1 == f2):
    print("Both files are Identical")
else:
    print("Not Identical")

# Question10
print("---------Question10---------")
with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Wipe.txt", "w") as f:
    f.write("")
print("Wipped")

# Question11
print("---------Question11---------")
with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Rename.txt", "r") as f:
    r = f.read()

with open("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\renamed_by_python.txt", "w") as f:
    f.write(r)

os.remove("E:\\Python\\Code\\Tutorial\\File Handling\\Practice\\Rename.txt")

print("Renamed")
