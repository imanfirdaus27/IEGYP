# first method

import mymodule

print(mymodule.add(10,20))
print(mymodule.minus(10,20))
print(mymodule.multiplication(10,20))
print(mymodule.divide(10,20))

# second method
from mymodule import add,minus,multiplication,divide
print(add(10,20))
print(minus(10,20))
print(multiplication(10,20))
print(divide(10,20))

# third method
from mymodule import *
print(add(10,20))
print(minus(10,20))
print(multiplication(10,20))
print(divide(10,20))

