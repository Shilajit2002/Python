'''
   ------ Multilevel Inheritance ------
   
            ----------------------
            | Grand Parent Class |
                      ^
                      |
               ----------------
               | Parent Class |
                      ^
                      |
               | Child Class |
               ---------------
            
'''


class GrandParent:
    def ancestors(self):
        print("Starting at 1960 from Grand Parent")

    def greet(self):
        print("Hello !! from Grand Parent Class")

    def showDetails(self):
        print("I am Grand Parent Class")

# Parent Class Extends Grand Parent Class


class Parent(GrandParent):
    def greet(self):
        print("Hello !! from Parent Class")

    def showDetails(self):
        print("I am Parent Class")

# Child Class Extends Parent Class


class Child(Parent):
    def showDetails(self):
        print("I am Child Class")


# Creating Child Class Object
C = Child()
# Call Child Class Show Details Method becuase it is overriding the Parent Class Method
C.showDetails()
# Call Parent Class Greet Method because Child have no Greet Method
C.greet()
# Call Grand Parent Class Greet Method because Parent & Child both have no Greet Method
C.ancestors()
