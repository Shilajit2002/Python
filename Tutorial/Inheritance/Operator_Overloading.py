class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets Add")
        return self.num+num2.num

    def __sub__(self, num2):
        print("Lets Subtract")
        return self.num-num2.num

    def __mul__(self, num2):
        print("Lets Multiply")
        return self.num*num2.num

    def __truediv__(self, num2):
        print("Lets Divide")
        return self.num/num2.num

    def __floordiv__(self, num2):
        print("Lets Floor Division")
        return self.num//num2.num


n1 = Number(10)
n2 = Number(2)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1//n2)
