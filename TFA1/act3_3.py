print("---- Please provide the details needed below ----")
fname = input("First name: ")
lname = input("Last name: ")
age = input("Age: ")
contactNo = input("Contact No.: ")
course = input("Course: ")
yearLevel = input("Year level: ")

stud_info = f"""┌──              STUDENT INFO             ──┐
Full name: {lname}, {fname}
Age: {age}
Contact No.: {contactNo}
Course and Year Level: {course} | {yearLevel}
└──                                       ──┘"""

f = open("students.txt", "a", encoding="utf-8")
f.write(stud_info)
f.close

print("\nStudent information has been saved to 'students.txxt'.")