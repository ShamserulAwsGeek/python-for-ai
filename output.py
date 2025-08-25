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


import sys
print(sys.version)


if 5 > 2:
  print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 


if 5 > 2:
 print("Five is greater than two!")
 print("Five is greater than two!")