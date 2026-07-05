#OOP is a programming paradigm that organizes code into objects that combine data (attributes) and behavior (methods)

class Person:
    name = "Shamserul"
    age = 29
    occupation = "Software Engineer"
    networth = 1000000

    def info(self):
        return f"{self.name} is a {self.age} year old {self.occupation} with a net worth of ${self.networth}."

a = Person()

print(a.info())
