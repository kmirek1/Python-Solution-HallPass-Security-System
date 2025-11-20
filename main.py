students=[" Jeremy", " Stacy", " Jenny", " Candace", " Ferb", " Candace"] #defines the list of students and the times that they have been out of the classroom 
minutes_out=[7, 10, 15, 8, 3, 4]

print("===HALL PASS SECURITY REPORT====")
statuses = []
notes=[]

for name, mins in zip(students, minutes_out):
    if mins<=5:
     status="OK"
    elif mins <=10:
     status="WARNING"
    else:
     status= "FLAGGED"

note="Duplicate name detected" if students.count(name)>1 else ""

statuses.append(status)
notes.append(note)

print(f"Student:{name}")
print(f"Time out:{mins}")
print(f"Status:{status}")

if note:
    print(f"Note:{note}")
print ()


average_time=sum(minutes_out)/len(minutes_out)
print("Average time in hallways: ", average_time)
