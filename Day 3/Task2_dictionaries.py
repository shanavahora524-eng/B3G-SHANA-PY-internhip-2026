student=[{"name":"Affiya","marks":88},
         {"name":"Jiya","marks":95},
         {"name":"Mahin","marks":91},]

top_student= student[0]

for student in student:
    if student["marks"] > top_student["marks"]:
        top_student = student

print("Highest Marks Student:",top_student)