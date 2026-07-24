# Multiple inheritance means a class can inherit from more than one parent class, 
# gaining attributes and methods from all of them.

#Basic example:
class A:
    def method_a(self):
        print("Method from A")

class B:
    def method_b(self):
        print("Method from B")

class C(A, B):   # C inherits from both A and B
    pass

obj = C()
obj.method_a()   # Method from A
obj.method_b()   # Method from B


-----------------------------------
-----------------------------------

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name of the Employee is {self.name}")
        

class Dancer():
    def __init__(self, dance_type):
        self.dance_type = dance_type

    def show(self):
            print(f"The dance type of the Dancer is {self.dance_type}")


class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance_type):
        Employee.__init__(self, name)
        Dancer.__init__(self, dance_type)  
   

o = DancerEmployee("Shamser", "Hip Hop")
o.show()  # This will call the show method from Employee class due to method resolution order
Dancer.show(o)  # This will call the show method from Dancer class
Employee.show(o)  # This will call the show method from Employee class
print(DancerEmployee.__mro__)  # This will print the method resolution order for DancerEmployee class

   




    
