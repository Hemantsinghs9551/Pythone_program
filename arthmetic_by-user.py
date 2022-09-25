import math
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def devide(x,y):
    return x/y
def multiply(x,y):
    return x*y

print("Select operation")
print("1-add")
print("2-subtract")
print("3-devide")
print("4-multiply")

while True:
    choice = input("Enter choice 1/2/3/4: ")
    if choice in ('1','2','3','4'):
        x  = int(input("enter the value for x: "))
        y = int (input("enter the value for y: "))
        
        if choice == '1':
            print(x,"+", y, "=", add(x,y))
        elif choice == '2':
            print(x,"-", y, "=", subtract(x,y))
             
        elif choice == '3':
            print(x,"/",y, "=", devide(x,y))
        elif choice == '4':
            print(x, "*",y, "=" ,multiply(x,y))
        else:
            print("choose a correct number.")
        
            

        
    

