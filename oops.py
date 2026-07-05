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
---------------------------------------------------

#Encapsulation:
#Bundling data and restricting direct access using private/protected attributes.
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance        #Private(name mangling) attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):     #controller access via methiod
        return self.__balance
    

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
#print(acc.__balance)  # This will raise an AttributeError since __balance is private

--------------------------------------------------------

#Inheritance:
# A child class inherits attributes and methods from a parent class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"
    

class Cat(Animal):       #Cat class inherits from Animal
    def speak(self):     #overriding the parent method of Animal class
        return f"{self.name} says Meow!"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

animals = [Cat("Whiskers"), Dog("Buddy"), Animal("Generic Animal")]
for animal in animals:
    print(animal.speak())



