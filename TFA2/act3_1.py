print("---- Please provide the details needed below ----")
fName = input("First name: ")
lName = input("Last name: ")
age = input("Age: ")

fullName = fName + " " + lName
print("\nFull name:", fullName)

slicedName = fName[slice(3)]
print("Sliced First Name:", slicedName)
greetings = f"Hello and welcome to the program, {slicedName}! You are currently {age}."
print(greetings)