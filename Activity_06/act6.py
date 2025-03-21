FILE_NAME = "items.txt"

class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return (f"Product ID: {self.item_id}\n"
                f"Product Name: {self.name}\n"
                f"Product Description: {self.description}\n"
                f"Product Price: Php {self.price:.2f}\n\n")

def get_next_item_id():
    try:
        file = open(FILE_NAME, "r")
        records = file.readlines()
        file.close()
        return int(records[-5].strip().split(": ")[1]) + 1 if records else 100
    except (FileNotFoundError, IndexError):
        return 100

def check_records_exist():
    try:
        file = open(FILE_NAME, "r")
        records = file.readlines()
        file.close()
        return bool(records)
    except FileNotFoundError:
        return False

def item_exists(item_id):
    try:
        file = open(FILE_NAME, "r")
        records = file.readlines()
        file.close()
        return any(records[i].strip().split(": ")[1] == str(item_id) for i in range(0, len(records), 5))
    except FileNotFoundError:
        return False

def add_item():
    print("\n--------------- ADD ITEM --------------")
    try:
        item = Item(
            get_next_item_id(),
            input("Enter the item name: ").strip(),
            input("Enter the item description: ").strip(),
            float(input("Enter the item price: ").strip())
        )
        if item.price < 0:
            print("Error: Price must be a positive number.")
            return

        file = open(FILE_NAME, "a")
        file.write(str(item))
        file.close()
        
        print(f"Item added successfully with ID: {item.item_id}")

    except ValueError:
        print("Error: Invalid input.")

def view_items():
    print("\n-------------- VIEW ITEMS -------------")
    if not check_records_exist():
        print("No records yet. Please add first.")
        return

    try:
        file = open(FILE_NAME, "r")
        records = file.read().strip()
        file.close()

        print(records if records else "No items found.")

    except FileNotFoundError:
        print("Error: No items found.")

def update_item():
    print("\n------------- UPDATE ITEM -------------")
    if not check_records_exist():
        print("No records yet. Please add first.")
        return

    try:
        item_id = input("Enter the item ID: ").strip()
        if not item_exists(item_id):
            print("Error: Item ID does not exist.")
            return

        file = open(FILE_NAME, "r")
        records = file.readlines()
        file.close()

        new_records = []
        updated = False

        for i in range(0, len(records), 5):
            if records[i].strip().split(": ")[1] == item_id:
                print("Leave blank if you don't want to change the field.")
                new_name = input(f"Enter new item name ({records[i+1].split(': ')[1].strip()}): ").strip() or records[i+1].split(": ")[1].strip()
                new_description = input(f"Enter new item description ({records[i+2].split(': ')[1].strip()}): ").strip() or records[i+2].split(": ")[1].strip()
                new_price = input(f"Enter new item price ({records[i+3].split(': ')[1].strip()}): ").strip() or records[i+3].split(": ")[1].strip()
                new_price = float(new_price)

                if new_price < 0:
                    print("Error: Price must be a positive number.")
                    return

                new_records.append(f"Product ID: {item_id}\nProduct Name: {new_name}\nProduct Description: {new_description}\nProduct Price: Php {new_price:.2f}\n\n")
                updated = True
            else:
                new_records.extend(records[i:i+5])

        file = open(FILE_NAME, "w")
        file.writelines(new_records)
        file.close()

        print("Item updated successfully." if updated else "No changes made.")

    except ValueError:
        print("Error: Invalid input.")

def delete_item():
    print("\n------------- DELETE ITEM --------------")
    if not check_records_exist():
        print("No records yet. Please add first.")
        return

    try:
        item_id = input("Enter the item ID: ").strip()
        if not item_exists(item_id):
            print("Error: Item ID does not exist.")
            return

        file = open(FILE_NAME, "r")
        records = file.readlines()
        file.close()

        new_records = [records[i:i+5] for i in range(0, len(records), 5) if records[i].strip().split(": ")[1] != item_id]
        file = open(FILE_NAME, "w")
        for record in new_records:
            file.writelines(record)
        file.close()

        print("Item deleted successfully.")

    except Exception as e:
        print(f"Error: {e}")

def search_item():
    print("\n------------- SEARCH ITEM ------------")
    if not check_records_exist():
        print("No records yet. Please add first.")
        return

    try:
        item_id = input("Enter the item ID: ").strip()
        if not item_exists(item_id):
            print("Error: Item ID does not exist.")
            return

        file = open(FILE_NAME, "r")
        records = file.readlines()
        file.close()

        for i in range(0, len(records), 5):
            if records[i].strip().split(": ")[1] == item_id:
                print("".join(records[i:i+5]))
                return

        print("Item not found.")

    except Exception as e:
        print(f"Error: {e}")

while True:
    print("\n---------- ITEM MANAGEMENT MENU ----------")
    print("   [1] Add Item     [2] View All Items")
    print("   [3] Search Item  [4] Update Item")
    print("   [5] Delete Item  [X] Exit")
    print("------------------------------------------")

    choice = input("Enter your choice: ").strip().upper()
    if choice == "1":
        add_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        search_item()
    elif choice == "4":
        update_item()
    elif choice == "5":
        delete_item()
    elif choice == "X":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")