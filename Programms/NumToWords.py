from num2words import num2words

with open("E:\\Python\\Code\\Programms\\Number.txt", "r") as file:
    file_content = file.read().strip()  # Read and strip any whitespace

try:
    number = int(file_content)
    word_representation = num2words(number)
    
    with open("E:\\Python\\Code\\Programms\\Number.txt", "w") as file:
        file.write(file_content+" "+word_representation)
except ValueError:
    print("The file does not contain a valid integer.")