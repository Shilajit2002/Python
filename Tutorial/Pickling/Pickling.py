# Import Pickle Module
import pickle

# Open the pickle file for Write Byte Mode
pickle_file = open(
    "E:\\Python\\Code\\Tutorial\\Pickling\\PickleFile.txt", "wb")

# A Dictionary
my_dict = {
    "Name": "Shilajit Acharjee",
    "Roll": 16500120028,
    "Dept": "Computer Science & Engineering"
}

# Store the dictionary in the pickle file as bytes
pickle.dump(my_dict, pickle_file)

# Open the pickle file for Read Byte Mode
pickle_file = open(
    "E:\\Python\\Code\\Tutorial\\Pickling\\PickleFile.txt", "rb")
# Store the byte data in new dict
new_dict = pickle.load(pickle_file)

print(new_dict)
