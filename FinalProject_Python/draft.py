# file to store the records
# wala ako maisip na variable name kaya FILE_NAME na lang (for now)
FILE_NAME = "records.txt"

# Function to count existing records
# #since may ginawa akong parang format sa pag-store ng records,
# ic-check niya kung ilan na yung existing records and kung wala pa, start sa 1 yung record number
# kung meron na, yung next record number na yung gagamitin

def count_existing_records():
    try:
        file = open(FILE_NAME, "r")
        content = file.read().strip()
        file.close()
        return content.count("Record #")  # Count occurrences of "Record #" to determine the next record number
    except FileNotFoundError:
        return 0  # If file doesn't exist, start at Record #1

    """
        Function to sign-up a new record
        
        mag-aask siya ng first name, middle name, last name, birthday, and gender
        then i-store niya yung record sa file in the requested format (which is kaartehan ko lang naman)
        
        then naisip ko ulit na what if maglagay tayo ng randomizer para mag-generate ng record number or
        like id nila? para yon nalang ilalagay sa search function and hindi na yung name?
    """
def sign_up():
    print("\n---------- SIGN-UP FORM ----------")
    try:
        first_name = input("Enter First Name: ").strip()
        middle_name = input("Enter Middle Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        birthday = input("Enter Birthday (MM/DD/YYYY): ").strip()
        gender = input("Enter Gender (M/F): ").strip().upper()

        # Simple validation lang ginawa ko rito para sa required fields
        # Kung may other idea ka paano mas magiging secure yung input, let me know or gawin mo na lang din
        if not first_name or not last_name or not birthday or gender not in ("M", "F"):
            print("Error: Invalid input. All fields are required.")
            return
        
        # Get the next record number
        record_number = count_existing_records() + 1

        # Store the record in the file in the requested format
        file = open(FILE_NAME, "a")
        file.write(f"\nRecord #{record_number}\n")
        file.write(f"Name: {first_name} {middle_name} {last_name}\n")
        file.write(f"Birthday: {birthday}\n")
        file.write(f"Gender: {gender}\n")
        file.close()

        print("Record successfully saved!")

    except Exception as e:
        print(f"Error: {e}")

    """
        Function to view all records
        
        mag-oopen siya ng file, then i-display niya yung laman exactly as stored
        kung wala siyang mababasa, sasabihin niya na walang records.
        
        Idk if you want pero pwede rin natin i-display kapag wala pang laman yung file
        na something "No records found. Please sign-up first." or something like that
    """ 
def view_records():
    print("\n---------- VIEW ALL RECORDS ----------")
    try:
        file = open(FILE_NAME, "r")
        records = file.read().strip()
        file.close()

        if not records:
            print("No records available.")
            return
        
        print(records)  # Display records exactly as stored

    except FileNotFoundError:
        print("No records found.")
    except Exception as e:
        print(f"Error: {e}")


    """
        Function to search a record
        
        mag-oopen siya ng file, then i-search niya yung first name or last name na nirequest
        kung may match, i-display niya yung full record. 
        kung wala, sasabihin niya na walang match. pero naisip ko rin uli na what if maglagay rin
        tayo ng "No records found. Please sign-up first." something ganon.
        
        then naisip ko rin what if may same name, so i-display niya lahat ng records na may same name? 
        or i-display niya lang yung first match? or idk tbh HWHAHSHAHHSD 
    """
def search_record():
    print("\n---------- SEARCH RECORD ----------")
    try:
        file = open(FILE_NAME, "r")
        records = file.readlines()
        file.close()

        search_name = input("Enter First Name or Last Name to search: ").strip().lower()
        found = False

        for i in range(len(records)):
            if "Name:" in records[i]:
                name = records[i].strip().split(": ")[1]
                if search_name in name.lower():
                    print("\n".join(records[i - 1 : i + 3]))  # Print the full record (4 lines: Record #, Name, Birthday, Gender)
                    found = True

        if not found:
            print("No matching record found.")

    except FileNotFoundError:
        print("No records found.")
    except Exception as e:
        print(f"Error: {e}")

# Main Menu natin (Main Class ganorn)
while True:
    print("\n----------------- MAIN MENU -----------------")
    print("   [1] Sign-up       [2] View all records")
    print("   [3] Search record [4] Exit")
    print("---------------------------------------------")

    try:
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            sign_up()
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

    except Exception as e:
        print(f"Error: {e}")