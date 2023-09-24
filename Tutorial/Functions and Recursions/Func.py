def func1():
    print("Hello World")

func1()

print("-------------------------")

def greet(name):
    gr="Hello "+name
    return gr

print(greet("Shilajit"))

print("-------------------------")

def avg(marks):
    return sum(marks)/(len(marks))

print("Average Marks =",avg([89,85,91,98]))

print("-------------------------")

l=["Car","Bike","Train","Bus"]

def loop(x):
    print(x*3)

def mapSimple(crazy,list):
    for item in list:
        crazy(item)

mapSimple(loop,l)