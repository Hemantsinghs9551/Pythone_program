x = int(input("Enter the range of dictonary: "))
student = {}

for i in range(x):
    name = input("Enter the name of student: ")
    sem = input("Enter the semester of the student: ")
    
    student[name] = sem
print(student)