# Karissa Mirek, Lizbeth Moran, Jocelyn Alvarez-Martinez, Alexis Salazar

students=[" Jeremy", " Stacy", " Jenny", " Candace", " Ferb", " Candace"] #defines the list of students and the times that they have been out of the classroom 
minutes_out=[7, 10, 15, 8, 3, 20]#defines the list of the minutes each students were out of the classroom

print("===HALL PASS SECURITY REPORT====") #prints ""===HALL PASS SECURITY REPORT====""
statuses = [] #stores the results
notes=[] # stores the results

for name, mins in zip(students, minutes_out): #logic to calculate staus and note
    if mins<=5: # sets up a condition for the mins 
         status="OK" # sets status as "OK"
    elif mins <=10: #sets up a condition if the other condition is incorrect
        status="WARNING" #sets status as "WARNING"
    else: # sets another condition if both conditions stated before are incorrect
        status= "FLAGGED" # sets status as "FLAGGED"

note="Duplicate name detected" if students.count(name)>1 else "" #sets note as "Duplicate name detected" is the students name appears more than once. Ex) Candace

statuses.append(status) #adds append to the list
notes.append(note) #adds note to the list 

print(f"Student:{name}") #prints "Student:{name of one of the students}" 
print(f"Time out:{mins} minutes") #prints "Time out:{mins out oft}"

if note: #sets condition for "note" the classroom} minutes"
# print(f"Status:{status}") #prints "Status:{status of the studen
    print(f"Note:{note}") # prints Note: {notes of the students}
print () #prints "duplicate name detceted"


average_time=sum(minutes_out)/len(minutes_out) #calculates the aveerage time student was in hallway
print("Average time in hallways: ", average_time)  # prints out the average time student spent in hallway

if average_time>=10: #sets condition for average_time
    status="FLAGGED" #sets status as the value "FLAGGED"
print(status) #prints "(status)"
