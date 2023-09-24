'''
   ------ Single Inheritance ------
   
            -------------
            | Base Class |
                  ^
                  |
          | Derived Class |
          -----------------
            
'''


class Parent:
    def greet(self):
        print("Hello !! from Parent Class")

    def showDetails(self):
        print("I am Parent Class")

# Child Class Extends Parent Class


class Child(Parent):
    def showDetails(self):
        print("I am Child Class")


# Creating Parent Class Object
P = Parent()
# Call Parent Class Show Details Method
P.showDetails()

# Creating Child Class Object
C = Child()
# Call Child Class Show Details Method becuase it is overriding the Parent Class Method
C.showDetails()
# Call Parent Class Greet Method because Child have no Greet Method
C.greet()
