from typing import Counter


# extract file type from file name(e.g: if input is "picture.jpeg , then output is jpeg")
x=input("Enter The File Name : ")
j=0
for i in x:
    j=j+1
    if i==".":
        print("File Extension is : '",x[j:],"'")
        break