import math

x = int(input("enter a number:"))
y = int(input("enter a number: "))
z = int(input("enter a number:"))

print("the number you entered : ",x,y,z)
if x>y and x>z:
    print("X is a greatest number: ",x)
elif y>x and y>z:
    print("the greatest number is y: ",y)
elif z>x and z>y:
    print("the greatest number is z: ",z)
else:
    print("the number are equal")
