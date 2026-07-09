#Instead of accessing a class attribute directly, you go through a method that can validate, transform, or protect the data.

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"The value is: {self._value}")
    
    #this is getter method:
    @property
    def ten_value(self):
        return 10*self._value
    
    #this is setter method:
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10

obj = MyClass(13)
obj.ten_value = 67  # Output: 130
print(obj.ten_value)  # Output: 130

--------------------------------------
--------------------------------------

# With Getter/Setter (Using @property)
# Python uses the @property decorator as the Pythonic way to implement getters and setters:

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # private attribute (convention: underscore)

    # Getter
    @property
    def age(self):
        return self._age

    # Setter
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person("John", 25)
print(p.age)   # 25 — calls getter
p.age = 30     # calls setter
p.age = -5     # raises ValueError


-------------------------------------
--------------------------------------
# @property — the Pythonic way to control access
# Instead of getters/setters, Python uses properties:
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):           # getter
        return self.__radius

    @radius.setter
    def radius(self, value):    # setter with validation
        if value < 0:
            raise ValueError("Radius can't be negative")
        self.__radius = value

c = Circle(5)
print(c.radius)   # 5  — clean attribute-style access
c.radius = 10     # calls setter
c.radius = -1     # ❌ ValueError


