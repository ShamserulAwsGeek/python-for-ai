# Multilevel inheritance is when a class inherits from a class that itself inherits from another class — forming a chain (A → B → C), 
# rather than one class inheriting from multiple parents at once (which is multiple inheritance, covered above).

A (grandparent)
   ↓
B (parent)
   ↓
C (child)

==========================
class Animal:
    def __init__(self, name,species):
        self.name = name
        self.species = species

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
    
   
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_info(self):
        Animal.show_info(self)
        print(f"Breed: {self.breed}")


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_info(self):
        Dog.show_info(self)
        print(f"Color: {self.color}")


o = GoldenRetriever("Tommy", "Golden")
o.show_info()


