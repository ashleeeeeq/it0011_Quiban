# Getting user input for a string containing digits
input_string = input("\n---- Please enter a string containing digits: ")

str_digit = 0

for char in input_string:
    if char.isdigit():  # check if the character is a digit
        str_digit += int(char) # add the digit to the sum

# Output the sum of digits in the string
print("\n┌──\t\t  RESULTS\t\t  ──┐\n")
print("\tSum of digits in the string:", str_digit)
print("\n└──\t\t\t\t\t  ──┘\n")