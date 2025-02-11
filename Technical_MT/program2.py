# Program to convert a date from the format DD/MM/YYYY to Month DD, YYYY
date_input = input("---- Enter a date with the format DD/MM/YYYY: ")
day, month, year = date_input.split("/") # Split the date into day, month, and year

# List of month names
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

# Convert month to index
month_name = month_names[int(month) - 1]

print(f"Date Output: {month_name} {int(day)}, {year}")