a = {
    "key": "value",
    "name": "Shilajit",
    "no": 16500120028,
    "list": [1, 2, 5, 6],
    "anotherdict": {
        "hello": "Greet",
        "sorry": "ok!!",
    }
}

print(a.keys())
print(a.values())
print(a.items())

updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "no": 4,
}

a.update(updateDict)

print(a)

print(a.get("name"))  # Prints value associated with key "name"
print(a["name"])  # Prints value associated with key "name"

# The difference between .get and [] syntax in Dictionaries?
print(a.get("name2"))  # Returns None as name2 is not present in the dictionary
print(a["name2"])  # throws an error as name2 is not present in the dictionary

a.pop("no")
print(a)