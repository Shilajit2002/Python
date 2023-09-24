import os

if (os.path.exists("E:\\Python\\Code\\Tutorial\\File Handling\\Create.txt")):
    os.remove("E:\\Python\\Code\\Tutorial\\File Handling\\Create.txt")
    print("Create.txt file has been deleted")
else:
    print("The Create.txt file does not exist")