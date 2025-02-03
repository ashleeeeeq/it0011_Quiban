try:
    file = open("students.txt", "r", encoding="utf-8")
    content = file.read()
    print("\nReading Student Infomation...\n")
    print(content)
    file.close()
except FileNotFoundError:
    print("The file 'students.txt' does not exist.")