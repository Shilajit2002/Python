class GrandParent:
    # Constructor
    def __init__(self):
        print("Hello !! from Grand Parent Class")

    def showDetails(self):
        print("I am Grand Parent Class")

# Parent Class Extends Grand Parent Class


class Parent(GrandParent):
    # Constructor
    def __init__(self):
        # This will Call Grand Parent Class Constructor
        super().__init__()
        print("Hello !! from Parent Class")

    def showDetails(self):
        # This will Call Grand Parent Show Details Method
        super().showDetails()
        print("I am Parent Class")

# Child Class Extends Parent Class


class Child(Parent):
    # Constructor
    def __init__(self):
        # This will Call Parent Class Constructor
        super().__init__()
        print("Hello !! from Child Class")

    def showDetails(self):
        # This will Call Parent Show Details Method
        super().showDetails()
        print("I am Child Class")


# Creating Child Class Object
C = Child()

C.showDetails()

'''
    Ans => Child Super Class is Parent Class so it will go to Parent Class then Parent Super Class is Grand Parent Class so it wil go to Grand Parent Class then Execute it and return to Parent Class then Execute it then return to Child Class then execute it.
'''
