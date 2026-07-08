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
