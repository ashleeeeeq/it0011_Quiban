input_string = input("\n---- Please enter a string containing digits: ")

str_digit = 0

for char in input_string:
    if char.isdigit():  
        str_digit += int(char) 

print("\n┌──\t\t  RESULTS\t\t  ──┐\n")
print("\tSum of digits in the string:", str_digit)
print("\n└──\t\t\t\t\t  ──┘\n")