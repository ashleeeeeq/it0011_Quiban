date_input = input("---- Enter a date with the format DD/MM/YYYY: ")
day, month, year = date_input.split("/")

month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

month_name = month_names[int(month) - 1]

print(f"Date Output: {month_name} {int(day)}, {year}")