#super()=  returns a proxy object that delegates method calls to a parent (or sibling) class. 
#It's the standard way to call inherited methods without hardcoding the parent class name.
class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

    
class ChildClass(ParentClass):

    def parent_method(self):
        print("Shamserul")
        super().parent_method()  # Calling the parent method from the child class

    def child_method(self):
        print("This is the child method.") 
        super().parent_method()  # Calling the parent method from the child class


child_object = ChildClass()
child_object.child_method()  # This will call the child method and then the parent method
child_object.parent_method()  # This will call the overridden parent method in the child class

-------------------------------------
-------------------------------------
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    
class Programmar(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language


e = Employee("Shamerul", 123)
p = Programmar("Mahenn", 124, "Python")

print(e.name, e.id)
print(p.name, p.id, p.language)
