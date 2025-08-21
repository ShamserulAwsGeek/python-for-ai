def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

closure = outer()
print(closure())
print(closure())
