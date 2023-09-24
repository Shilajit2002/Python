# Reading Text File
f = open("E:\\Python\\Code\\Tutorial\\File Handling\\Hello.txt", "r")
text = f.read()
print("Hello.txt is =", text)
f.close()

print("-------------------------------------------")

# Reading Image File
fi = open("E:\\Python\\Code\\Tutorial\\File Handling\\Image.jpeg", "rb")
img = fi.read()
print("Image.jpg is =", img)
fi.close()

print("-------------------------------------------")

# Reading Pdf File
fp = open("E:\\Python\\Code\\Tutorial\\File Handling\\Text.pdf", "rb")
pdf = fp.read()
print("Text.pdf is =", pdf)
fp.close()
