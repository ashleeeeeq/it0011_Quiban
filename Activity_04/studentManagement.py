students = []
menu = (f"""{"\n"}      ------ STUDENT RECORD MANAGEMENT SYSTEM ------{"\n"}
            [1] Open File
            [2] Save File
            [3] Save as File
            [4] Show All Students Record
            [5] Show Student Record
            [6] Add Student Record
            [7] Edit Student Record
            [8] Delete Student Record
            [0] Exit {"\n"}
    ---------------------------------------------------""")

while True:
    print(menu)
    
    userInput = input("    ---- Enter your choice: ")
    print("\n")
    
    if userInput == '1':
        try:
            file = open('studentRecords.txt', 'r')
            students = [eval(line.strip()) for line in file.readlines()]
            file.close()
            print("\tFile opened successfully.")
        except FileNotFoundError:
            print("\tThe file does not exist.")
    
    elif userInput == '2':
        try:
            file = open('studentRecords.txt', 'w')
            for student in students:
                file.write(str(student) + "\n")
            file.close()
            print("\tFile saved successfully.")
        except Exception as e:
            print(f"\tAn error occurred: {e}")
    
    elif userInput == '3':
        filename = input("\tEnter new file name: ")
        file = open(filename, 'w')
        for student in students:
            file.write(str(student) + "\n")
        file.close()
        print(f"\tFile saved as {filename} successfully.")
            
    elif userInput == '4':
        print(f"""{"\t"} OPTIONS FOR DISPLAYING ALL RECORDS
            [1] Display records ordered by last name
            [2] Display records ordered by grade
        ---------------------------------------------""")
        sub_choice = input("\tEnter your choice: ")
        
        if sub_choice == '1':
            # Sort by last name
            print("\n\tSTUDENT RECORDS (Sorted by Last Name)")
            print("\t------------------------------------------------------------")
            print("\tID\tLast Name\tFirst Name\tClass Standing\tExam Grade")
            print("\t------------------------------------------------------------")
            for i in range(len(students)):
                for j in range(i + 1, len(students)):
                    if students[i][1][1] > students[j][1][1]:
                        students[i], students[j] = students[j], students[i]
                        
            for student in students:
                print(f"\t{student[0]}\t{student[1][1]}\t\t{student[1][0]}\t\t{student[2]}\t\t{student[3]}")
                
        elif sub_choice == '2':
            # Sort by grade
            print("\n\tSTUDENT RECORDS (Sorted by Grade)")
            print("\t------------------------------------------------------------")
            print("\tID\tLast Name\tFirst Name\tClass Standing\tExam Grade")
            print("\t------------------------------------------------------------")
            for i in range(len(students)):
                for j in range(i + 1, len(students)):
                    grade_i = students[i][2] * 0.6 + students[i][3] * 0.4
                    grade_j = students[j][2] * 0.6 + students[j][3] * 0.4
                    if grade_i > grade_j:
                        students[i], students[j] = students[j], students[i]
                        
            for student in students:
                print(f"\t{student[0]}\t{student[1][1]}\t\t{student[1][0]}\t\t{student[2]}\t\t{student[3]}")
        
    elif userInput == '5':
        student_id = input("\tEnter student ID: ")
        found = False
        for student in students:
            if student[0] == student_id:
                print(f"\t\nStudent Record Found:\n\tID: {student[0]}\n\tName: {student[1][0]} {student[1][1]}\n\tClass Standing: {student[2]}\n\tExam Grade: {student[3]}")
                found = True
                break
        if not found:
            print("\tStudent not found.")
            
    elif userInput == '6':
        student_id = input("\tEnter student ID (6 digits): ")
        if len(student_id) != 6 or not student_id.isdigit():
            print("\tInvalid student ID. It must be a 6-digit number.")
            continue
        
        student_fName = input("\tEnter student first name: ")
        student_lName = input("\tEnter student last name: ")
        class_standing = float(input("\tEnter student class standing: "))
        exam_grade = float(input("\tEnter student major exam grade: "))
        students.append([student_id, (student_fName, student_lName), class_standing, exam_grade])
        print("\tStudent record added successfully.")
        
    elif userInput == '7':
        student_id = input("\tEnter student ID to edit: ")
        found = False
        for index, student in enumerate(students):
            if student[0] == student_id:
                student_fName = input("\tEnter student first name: ")
                student_lName = input("\tEnter student last name: ")
                class_standing = float(input("\tEnter student class standing: "))
                exam_grade = float(input("\tEnter student major exam grade: "))
                students[index] = [student_id, (student_fName, student_lName), class_standing, exam_grade]
                print("\tStudent record updated successfully.")
                found = True
                break
        if not found:
            print("\tStudent not found.")
            
    elif userInput == '8':
        student_id = input("\tEnter student ID to delete: ")
        found = False
        for student in students:
            if student[0] == student_id:
                students.remove(student)
                print("\tStudent record deleted successfully.")
                found = True
                break
        if not found:
            print("\tStudent not found.")
            
    elif userInput == '0':
        break
    
    else:
        print("\tInvalid input. Please try again.")