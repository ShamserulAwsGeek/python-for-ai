#OOP is a programming paradigm that organizes code into objects that combine data (attributes) and behavior (methods)

class Person:
    name = "Shamserul"
    age = 29
    occupation = "Software Engineer"
    networth = 1000000

    def info(self):
        return f"{self.name} is a {self.age} year old {self.occupation} with a net worth of ${self.networth}."

a = Person()
b = Person()
b.name = "Maheen"
b.age = 25
b.occupation = "Chef"
b.networth = 50000

print(a.info())
print(b.info())

#Classes & Objects:
#A class is a blueprint; an object is an instance of that blueprint.
class Person:
    def __init__(self, name, occupation):  # Constructor-  it is also called as Dunder method.
        self.name = name              # Instance attribute
        self.occupation = occupation

    def info(self):
        return f"{self.name} is a {self.occupation}"

# Creating objects:
a = Person("Shamserul", "Developer")
b = Person("Maheen", "Chef")

print(a.info())
print(b.info())
