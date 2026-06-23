Student=[("Riya",88),("Aman",95),("Sara",72)]
Sorted=sorted(Student,key=lambda X:X[1],reverse=True)

print("Student sorted by marks:")
for name,marks in Sorted:
    print(name,"-",marks)

