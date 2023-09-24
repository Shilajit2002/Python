# User Input
a=input("Enter Your Name : ")
print("** Good Afternoon " + a + " :) **")

# Letter Template
name=input("Enter Your Name : ")
date=input("Enter Date : ")
letter='''\nDear <|NAME|> ,
    You are Selected !

    \tDate: <|DATE|>'''
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)

# Find Double Spaces
space="Hello  World  !"
print("First Occurence of Double Space is : ",space.find("  "))
print("Last Occurence of Double Space is : ",space.rfind("  "))

# Replace double space in single space
print("After replacing string is : ",space.replace("  "," "))

# Format a letter using escape sequence
x="Dear \'Bob\',\n\tThis Python Course is nice.\nThanks!"
print(x)