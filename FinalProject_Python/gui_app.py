import tkinter as tk
from tkinter import messagebox, ttk

FILENAME = "records.txt"

def load_records():
    records = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    records.append({
                        "First Name": parts[0],
                        "Middle Name": parts[1],
                        "Last Name": parts[2],
                        "Birthday": parts[3],
                        "Gender": parts[4]
                    })
    except FileNotFoundError:
        pass
    return records

def save_records(records):
    with open(FILENAME, "w") as file:
        for record in records:
            file.write(f"{record['First Name']}|{record['Middle Name']}|{record['Last Name']}|{record['Birthday']}|{record['Gender']}\n")

def sign_up():
    def submit():
        try:
            first_name = first_name_entry.get().strip()
            middle_name = middle_name_entry.get().strip()
            last_name = last_name_entry.get().strip()
            birthday = birthday_entry.get().strip()
            gender = gender_var.get()
            
            if not first_name or not last_name or not birthday:
                raise ValueError("First name, last name, and birthday are required.")
            
            new_record = {
                "First Name": first_name,
                "Middle Name": middle_name,
                "Last Name": last_name,
                "Birthday": birthday,
                "Gender": gender
            }
            
            records = load_records()
            records.append(new_record)
            save_records(records)
            
            messagebox.showinfo("Success", "Record added successfully!")
            sign_up_window.destroy()
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    
    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")
    
    tk.Label(sign_up_window, text="First Name:").grid(row=0, column=0)
    first_name_entry = tk.Entry(sign_up_window)
    first_name_entry.grid(row=0, column=1)
    
    tk.Label(sign_up_window, text="Middle Name:").grid(row=1, column=0)
    middle_name_entry = tk.Entry(sign_up_window)
    middle_name_entry.grid(row=1, column=1)
    
    tk.Label(sign_up_window, text="Last Name:").grid(row=2, column=0)
    last_name_entry = tk.Entry(sign_up_window)
    last_name_entry.grid(row=2, column=1)
    
    tk.Label(sign_up_window, text="Birthday (YYYY-MM-DD):").grid(row=3, column=0)
    birthday_entry = tk.Entry(sign_up_window)
    birthday_entry.grid(row=3, column=1)
    
    tk.Label(sign_up_window, text="Gender:").grid(row=4, column=0)
    gender_var = tk.StringVar(value="Other")
    gender_menu = ttk.Combobox(sign_up_window, textvariable=gender_var, values=["Male", "Female", "Other"])
    gender_menu.grid(row=4, column=1)
    
    tk.Button(sign_up_window, text="Submit", command=submit).grid(row=5, columnspan=2)

def view_records():
    records = load_records()
    view_window = tk.Toplevel(root)
    view_window.title("All Records")
    
    text_area = tk.Text(view_window, width=50, height=20)
    text_area.pack()
    
    if records:
        for record in records:
            text_area.insert(tk.END, f"{record}\n\n")
    else:
        text_area.insert(tk.END, "No records found.")

def search_record():
    def search():
        query = search_entry.get().strip().lower()
        records = load_records()
        results = [rec for rec in records if query in rec["First Name"].lower() or query in rec["Last Name"].lower()]
        
        result_text.delete("1.0", tk.END)
        if results:
            for record in results:
                result_text.insert(tk.END, f"{record}\n\n")
        else:
            result_text.insert(tk.END, "No matching records found.")
    
    search_window = tk.Toplevel(root)
    search_window.title("Search Records")
    
    tk.Label(search_window, text="Enter name to search:").pack()
    search_entry = tk.Entry(search_window)
    search_entry.pack()
    
    tk.Button(search_window, text="Search", command=search).pack()
    
    result_text = tk.Text(search_window, width=50, height=10)
    result_text.pack()

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Record Management System")

tk.Label(root, text="Menu", font=("Arial", 14)).pack()

tk.Button(root, text="Sign Up", command=sign_up).pack()

tk.Button(root, text="View All Records", command=view_records).pack()

tk.Button(root, text="Search Record", command=search_record).pack()

tk.Button(root, text="Exit", command=exit_app).pack()

root.mainloop()