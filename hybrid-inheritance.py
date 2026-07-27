#Hybrid Inheritance: Hybrid inheritance is a combination of two or more types of inheritance (like multiple,
#multilevel, and hierarchical) within the same class hierarchy
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


class Employee(Person):
    def __init__(self, name, employee_id):
        Person.__init__(self, name)
        self.employee_id = employee_id

    def show_id(self):
        print(f"Employee ID: {self.employee_id}")
        

class Freelancer(Person):
    def __init__(self, name, project):
        Person.__init__(self, name)
        self.project = project

    def show_project(self):
        print(f"Project: {self.project}")

class Consultant(Freelancer):
    def __init__(self, name, project, hourly_rate):
        Freelancer.__init__(self, name, project)
        self.hourly_rate = hourly_rate

    def show_rate(self):
        print(f"Hourly Rate: ${self.hourly_rate}")


c = Consultant("Shamserul", "AI Development", 50)
c.display()
c.show_project()
c.show_rate()

-----------------------------
-----------------------------
class A:
    def method_a(self):
        print("Method A from class A")

class B(A):              # Single inheritance (B inherits A)
    def method_b(self):
        print("Method B from class B")

class C(A):               # Hierarchical inheritance (C also inherits A)
    def method_c(self):
        print("Method C from class C")

class D(B, C):             # Multiple inheritance (D inherits B and C)
    def method_d(self):
        print("Method D from class D")


obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()

print(D.__mro__)  # Method Resolution Order
