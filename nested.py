x = int(input("enter the size of list1: "))
y = int(input("enter the size of list2: "))
list1=[]
list2=[]
for i in range(x):
    for j in range(y):
        list2.append(input())
    list1.append(list2)
    list2=[]
print (list1)
