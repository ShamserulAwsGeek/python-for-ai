x =4
print(x)

def hello():
    x = 5
    print(f" the local x is: {x}")
    print("Hello, World!")

hello()

print(f" the global x is: {x}")


x =10 #global varibale
def my_function():
    global x  #global varibale
    x = 15
    global y
    y= 20  #local varibale
    print(f" the local y is: {y}")
    print("Hello, World!")
my_function()

print(f" the global x is: {x}")
print(f" the global y is: {y}")


