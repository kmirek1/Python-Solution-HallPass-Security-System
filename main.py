# Karissa Mirek, Lizbeth Moran, Jocelyn Alvarez-Martinez, Alexis Salazar

students=[" Jeremy", " Stacy", " Jenny", " Candace", " Ferb", " Candace"] #defines the list of students  
minutes_out=[7, 10, 15, 8, 3, 20]#defines the list of the minutes each students were out of the classroom

print("===HALL PASS SECURITY REPORT====") #prints ""===HALL PASS SECURITY REPORT====""
statuses = [] #stores the results
notes=[] # stores the results

for name, mins in zip(students, minutes_out): #logic to calculate staus and note
    if mins <= 5:# sets up a condition for the mins 
        status_of_student="OK" # sets status as "OK"
    elif mins <= 10:#sets up a condition if the other condition is incorrect
        status_of_student="WARNING" #sets status as "WARNING"
    else: # sets another condition if both conditions stated before are incorrect
        status_of_student= "FLAGGED" # sets status as "FLAGGED"
    if students.count(name) > 1:#sets up a condition to find duplicate names
        note = "Duplicate name detected" #sets note as "Duplicate name detected" is the students name appears more than once. Ex) Candace
    else:
        note = ""

    statuses.append(status_of_student)#adds append to the list
    notes.append(note)#adds note to the list 

    print(f"Students: {name}")#prints "Student:{name of one of the students}" 
    print(f"Minutes out: {mins} minutes")#prints "Time out:{mins out oft}"
    print(f"Status: {status_of_student}")

    if note: #sets condition for "note" the classroom} minutes"
        print(f"Note: {note}")# prints Note: {notes of the students}
    print() #prints "duplicate name detceted"

average_time=sum(minutes_out)/len(minutes_out) #calculates the aveerage time student was in hallway
print("Average time in hallways: ", average_time)  # prints out the average time student spent in hallway
if average_time>=10: #sets condition for average_time
    status="FLAGGED" #sets status as the value "FLAGGED"
    print(status) #prints "(status)"
