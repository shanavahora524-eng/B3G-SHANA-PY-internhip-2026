task=[]

task.append("complete python Assignment")
task.append("Study for Exam")
task.append("Weak up Early")
task.append("Practice Python Coding")
task.append("Exercise for 30 Minutes")

print("Task After Adding:")
for item in task:
    print("-",item)

task.remove("Study for Exam")
task.remove("Weak up Early")

print("\nTask After removing:")
for item in task:
    print("-",item)