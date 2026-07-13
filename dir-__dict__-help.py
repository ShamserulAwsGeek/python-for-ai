#Python's Built-in Inspection Tools:
#dir() = Returns a list of names (attributes, methods) in the current scope or of an object.

class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return "Woof!"

d = Dog("Rex")
print(dir(d))
# ['__class__', '__init__', ..., 'bark', 'name']

# Filter out dunder methods to see only user-defined ones
print([x for x in dir(d) if not x.startswith("__")])
# ['bark', 'name']
print(d.bark())  # Output: Woof!

------------------------------------------
------------------------------------------
#__dict__ = A dictionary holding an object's (or class's) own namespace — only the attributes directly defined on it, not inherited ones.
class Animal:
    species = "Canine"          # class attribute

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name        # instance attributes
        self.age = age

d = Dog("Rex", 3)

print(d.__dict__)               # instance's own attributes
# {'name': 'Rex', 'age': 3}

print(Dog.__dict__)             # class's own namespace
# {'__init__': <function>, ...}  — does NOT include 'species' from Animal

print(Animal.__dict__)          # Animal's own namespace
# {'species': 'Canine', '__dict__': ..., ...}

-------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1.0


p = Person("Shamserul", 30)
print(p.__dict__)

------------------------------
------------------------------

#help() = Displays the docstring-based documentation for any object, function, class, or module — powered by pydoc.

def add(a, b):
    """
    Add two numbers and return the result.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of a and b.

    """
    return a + b

help(add)
print(add(3, 5))

help(str)
help(str.split)
help("modules")

-------------------------------
------------------------------
#Combining All Three:
import math

dir(math)           # what names does math have?
math.__dict__       # name → actual object mapping
help(math.sqrt)     # how do I use sqrt?

# Use dir() to discover what's available
# Use __dict__ to inspect an object's own data
# Use help() to understand how something works
