# Hierarchical inheritance is when multiple child classes inherit from a single parent class.
# It's the opposite structure of multiple inheritance — one base, many derived classes.

        Parent
       /   |   \
    Child1 Child2 Child3


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        return f"{self.brand} is a vehicle"
    

class Car(Vehicle):
    def car_type(self):
        print("This is a car")

class Truck(Vehicle):
    def truck_type(self):
        print("This is a truck")


class Motorcycle(Vehicle):
    def motorcycle_type(self):
        print("This is a motorcycle")


c = Car("Toyota")
print(c.display_info())
c.car_type()

t = Truck("Ford")
print(t.display_info())
t.truck_type()

m = Motorcycle("Harley-Davidson")
print(m.display_info())
m.motorcycle_type()



