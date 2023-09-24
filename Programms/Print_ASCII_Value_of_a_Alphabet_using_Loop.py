# Enter one Alphabet, Output will be 'ASCII' of that Alphabet...using Loop...Not use ord function

alpha = input("Enter a Alphabet : ")
for i in range(65, 123):
    if chr(i) == alpha:
        print("The ASCII Value of " +alpha+ " is : ", i)