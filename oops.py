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
-----------------------------------------------------------

#Polymorphism:
#The same interface works differently depending on the object type.
class Shape:
    def area(self):
        raise NotImplementedError
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
Shapes = [Circle(5), Rectangle(4, 6)]
for shape in Shapes:
    print(f"The area of the shape is: {shape.area()}")

-----------------------------------------------------------

#Dunder Method:
# Magic methods let you define how objects behave with built-in operations.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)
    
v1 = Vector(2,  4)
v2 = Vector(3,  4)

print(v1 + v2)  
print(len(v1))



