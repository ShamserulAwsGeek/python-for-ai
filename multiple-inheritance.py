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
