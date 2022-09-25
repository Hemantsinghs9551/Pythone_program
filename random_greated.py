import random
import math

x = (random.randint(0,9))
y = (random.randint(0,9))
z = (random.randint(0,9))

print(x)
print(y)
print(z)

if x>y and x>z:
    print("X is a greatest number: ",x)
elif y>x and y>z:
    print("the greatest number is y: ",y)
elif z>x and z>y:
    print("the greatest number is z: ",z)
else:
    print("the number are equal")