a={
    "key":"value",
    "name":"Shilajit",
    "no":16500120028,
    "list":[1,2,5,6],
    "anotherdict":{
        "hello":"Greet",
        "sorry":"ok!!",
    }
}

print(a)
print(a["anotherdict"])
print(a["anotherdict"]["hello"])
print(a["list"])
print(a["name"])
print(a["no"])

# Update a Key value
a["key"]="new Value"

print(a["key"])

print(type(a))