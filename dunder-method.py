# Dunder = Double underscore. Methods wrapped with double underscores on both sides, like __init__, __str__, etc.
# They are also called magic methods or special methods.
# They let your custom classes behave like built-in Python types. 
# Python calls them automatically behind the scenes — you never call them directly.

class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i    
    
    def __str__(self):
        return f"Employee name is {self.name} str"
    
   
e = Employee("Shamserul")
print(str(e))
print(len(e))
print(e.name)

---------------------------------
---------------------------------
class Dog:
    def __init__(self, name, age):   # called when you create an object
        self.name = name
        self.age = age

    def __str__(self):               # called when you print the object
        return f"{self.name}, Age: {self.age}"

    def __len__(self):               # called when you use len()
        return self.age

dog = Dog("Bruno", 3)

print(dog)       # Bruno, Age: 3   ← __str__ fired automatically
print(len(dog))  # 3               ← __len__ fired automatically

----------------------------
---------------------------
class Bag:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):         # called when you use +
        return Bag(self.items + other.items)

bag1 = Bag(["apple", "banana"])
bag2 = Bag(["mango"])

bag3 = bag1 + bag2                    # __add__ fires automatically
print(bag3.items)  # ["apple", "banana", "mango"]
