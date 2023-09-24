'''
   ------ Multiple Inheritance ------
   
            ----------------  ----------------
            | Base Class 1 |  | Base Class 2 | 
                        ^       ^
                        |       |
                    | Derived Class |
                    -----------------
            
'''


class Father:
    def greet(self):
        print("Hello !! from Father Class")

    def showDetails(self):
        print("I am Father Class")


class Mother:
    def greet(self):
        print("Hello !! from Mother Class")

    def showDetails(self):
        print("I am Mother Class")

# Son Class Extends Father & Mother Class


class Son(Father, Mother):
    def showDetails(self):
        print("I am Son Class")


# Creating Son Class Object
S = Son()
# Call Son Class Show Details Method becuase it is overriding the Father & Mother Class Method
S.showDetails()
# Call Father Class Greet Method because Son have no Greet Method and Son Class extends Father Class First
S.greet()

# Daughter Class Extends Mother & Father Class


class Daughter(Mother, Father):
    def showDetails(self):
        print("I am Daughter Class")


# Creating Daughter Class Object
D = Daughter()
# Call Daughter Class Show Details Method becuase it is overriding the Mother & Father Class Method
D.showDetails()
# Call Mother Class Greet Method because Daughter have no Greet Method and Daughter Class extends Mother Class First
D.greet()
