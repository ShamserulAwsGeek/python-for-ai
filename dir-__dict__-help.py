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
