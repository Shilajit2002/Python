# Write
fw = open("E:\\Python\\Code\\Tutorial\\File Handling\\New.txt", "w")

fw.write("This is new Text file")
fw.close()

# Write
f = open("E:\\Python\\Code\\Tutorial\\File Handling\\New.txt", "w")

f.write("This is updated Text file")
f.close()

# Append
fa = open("E:\\Python\\Code\\Tutorial\\File Handling\\New.txt", "a")

fa.write("\nThis is a extra line in the New.txt")
fa.close()
