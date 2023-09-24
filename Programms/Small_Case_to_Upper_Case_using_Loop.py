# Enter a alphabet in Small case..output will be upper case
x = input("Enter a Small letter Alphabet : ")
print("Upper Case of this : ")
for i in x:
    for j in range(97, 123):
        if chr(j) == i:
            print(chr(j-32))