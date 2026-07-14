# Method Overriding = A child class redefines a method that already exists in its parent class

#Simple Analogy:

# A parent says "greet everyone politely."
# The child says "No, I'll greet in my own way."
# The child's version overrides the parent's version.

class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
     
    def __init__(self, radius):
        super().__init__(radius, radius)
        self.radius = radius

    def area(self):
        return 3.14 * super().area()


circle = Circle(3)
print("Area of circle:", circle.area())
    
sqr = Shape(5, 5)
print("Area of square:", sqr.area())
       




    
