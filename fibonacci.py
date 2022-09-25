import math
no_of_term = int(input("Enter the number of terms: "))
n1,n2= 0,1
count = 0

while count<=no_of_term:
    
    print(n1)
    nth = n1+n2
    n1 = n2
    n2 = nth
    count += 1
    print("fabonacci series is : ")
