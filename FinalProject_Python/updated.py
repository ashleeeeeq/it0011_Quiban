# NOTE1: This is the updated version
# NOTE2: Nag-add lang ako ng condition sa pag-check ng records_exist sa view_records at search_record

class Record_Logs:
    def __init__(self, file_name="records.txt"):  # forda class parang bongga
        self.records_inputs = file_name

    # Function to count existing records
    def count_existing_records(self):
        try:
            with open(self.records_inputs, "r") as file:
                content = file.read().strip()
            return content.count("Record #")  # Count occurrences of "Record #" to determine the next record number
        except FileNotFoundError:
            return 0  # If file doesn't exist, start at Record #1

    # Function to check if records exist
    def records_exist(self):
        return self.count_existing_records() > 0

    # Function to sign-up a new record
    def sign_up(self):
        print("\n---------- SIGN-UP FORM ----------")
        try:
            first_name = input("Enter First Name: ").strip()
            middle_name = input("Enter Middle Name: ").strip()
            last_name = input("Enter Last Name: ").strip()

            # Loop until a valid birthday format is entered
            while True:
                birthday = input("Enter Birthday (MM-DD-YYYY): ").strip()

                if len(birthday) != 10 or birthday[2] != '-' or birthday[5] != '-':
                    print("Error: Birthday must be in MM-DD-YYYY format with hyphens.\n")
                    continue

                month, day, year = birthday.split('-')

                if not (month.isdigit() and day.isdigit() and year.isdigit()):
                    print("Error: Birthday must contain only numbers and hyphens.\n")
                    continue

                month, day, year = int(month), int(day), int(year)

                if month < 1 or month > 12:
                    print("Error: Month must be between 01 and 12.\n")
                    continue
                if day < 1 or day > 31:
                    print("Error: Day must be between 01 and 31.\n")
                    continue
                if year < 1900 or year > 2100:
                    print("Error: Year must be a valid four-digit number.\n")
                    continue

                break  # Exit loop once valid

            # Loop until a valid gender is entered
            while True:
                gender = input("Enter Gender (M/F): ").strip().upper()
                if gender in ("M", "F"):
                    break  # Exit loop when valid input is provided
                else:
                    print("Error: Gender must be 'M' for Male or 'F' for Female.\n")

            # Convert gender to full word
            gender_full = "Male" if gender == "M" else "Female"

            record_number = self.count_existing_records() + 1
            unique_id = "2025" + str(record_number).zfill(5)

            with open(self.records_inputs, "a") as file:
                file.write(f"\nRecord #{record_number}\n")
                file.write(f"ID: {unique_id}\n")
                file.write(f"Name: {first_name} {middle_name} {last_name}\n")
                file.write(f"Birthday: {birthday}\n")
                file.write(f"Gender: {gender_full}\n")

            print(f"\nID: {unique_id}")
            print("Record successfully saved!")
        except Exception as e:
            print(f"Error: {e}")

    # Function to view all records
    def view_records(self):
        if not self.records_exist():
            print("\nNo records found. Please sign-up first.")
            return

        print("\n---------- VIEW ALL RECORDS ----------")
        try:
            with open(self.records_inputs, "r") as file:
                records = file.read().strip()

            if not records:
                print("No records found. Please sign-up first.")
                return

            print(records)  # Display records exactly as stored
        except FileNotFoundError:
            print("No available records at the moment.")
        except Exception as e:
            print(f"Error: {e}")

    # Function to search a record 
    # Instead of first name / last name, i used ID to search the record
    def search_record(self):
        if not self.records_exist():
            print("\nNo records found. Please sign-up first.")
            return

        print("\n---------- SEARCH RECORD BY ID ----------")
        try:
            with open(self.records_inputs, "r") as file:
                records = file.readlines()

            search_id = input("Enter ID to search: ").strip()
            found = False

            for i in range(len(records)):
                if "ID:" in records[i]:
                    record_id = records[i].strip().split(": ")[1]
                    if search_id == record_id:
                        print("".join(records[i - 1 : i + 4]))  # Display the full record (fixed format)
                        found = True
                        break  # Exit loop after finding the record

            if not found:
                print("No matching record found. Please check if the ID is correct.")

        except FileNotFoundError:
            print("No available records at the moment.")
        except Exception as e:
            print(f"Error: {e}")

# Main Menu
def main():  # The main function para sa pinaka nilalamang logic
    logs = Record_Logs()
    while True:
        print("\n----------------- MAIN MENU -----------------")
        print("   [1] Sign-up       [2] View all records")
        print("   [3] Search record [X] Exit")
        print("---------------------------------------------")

        try:
            choice = input("Enter your choice: ").strip().upper()
            if choice == "1":
                logs.sign_up()
            elif choice == "2":
                logs.view_records()
            elif choice == "3":
                logs.search_record()
            elif choice == "X":
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__": 
    main()  # Calls the main function only if the script is run as the main program