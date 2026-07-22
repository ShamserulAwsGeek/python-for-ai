# Single inheritance is when a class (child/derived class) inherits from only one parent (base) class. 
# This is the simplest and most common form of inheritance.


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} barks.")



d = Dog("Doggo", "Labrador")
d.make_sound()  # Output: Doggo barks.


a = Animal("Generic Animal", "Unknown")
a.make_sound()  # Output: Generic Animal makes a sound.


----------------------------
-----------------------------

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")


class Child(Parent):  # Single inheritance
    def __init__(self, name, age):
        super().__init__(name)  # calls Parent's __init__
        self.age = age

    def show_age(self):
        print(f"I am {self.age} years old")


c = Child("Sham", 30)
c.greet()      # inherited from Parent
c.show_age()   # defined in Child



