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
