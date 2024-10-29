import math

def add(x, y):
    return x + y

def product(x, y):
    return x * y

def lcm(x, y):
    if(y == 0): 
        return 0
    return math.lcm(x, y)

print (add(2, 5))
print (product(2, 5))
print (lcm(2, 5))
