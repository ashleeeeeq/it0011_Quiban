# First name Last name Middle name Birthday Gender Address Course Year level 

print("---- Please provide the details needed below ----")
f_name = input("First name: ")
l_name = input("Last name: ")
i_name = input("Middle name: ")
bday = input("Birthday (MM-DD-YYYY): ")
gender = input("Gender (M/F): ")
address = input("Address: ")
course = input("Course: ")
yearLevel = input("Year level: ")

print("\n┌──              STUDENT INFO             ──┐\n")
print("Student name:", l_name, ",", f_name, i_name)
print("Course and year level:", course, "|", yearLevel)
print("Gender:", gender)
print("Birthday:", bday)
print("Address:", address)
print("\n└──                                       ──┘")

