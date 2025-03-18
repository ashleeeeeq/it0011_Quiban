# for divide function 
def divide(num1, num2):
    if num2 == 0:
        print("Error: Denominator cannot be zero.") # Error message
        return None
    return num1 / num2

# for exponent function
def exponentiate(base, exponent):
    return base ** exponent

# for modulo / remainder function
def remainder(num1, num2):
    if num2 == 0:
        print("Error: Denominator cannot be zero.")
        return None
    return num1 % num2

# for summation ; sum of all numbers from start to end, like a range from start to end
def summation(start, end):
    if start > end:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(start, end + 1))

# Menu
while True:
    print("\n---------- MATHEMATICAL MENU ----------")
    print("   [D] Divide     [E] Exponentiation")
    print("   [R] Remainder  [F] Summation")
    print("   [X] Exit")
    print("---------------------------------------")
    
    choice = input("Enter your choice: ").strip().upper()
    
    if choice == "D":  # Division
        num1 = float(input("\nEnter numerator: "))
        num2 = float(input("Enter denominator: "))
        result = divide(num1, num2)
        if result is not None:
            print("Result:", result)

    elif choice == "E":  # Exponentiation
        base = float(input("\nEnter base: "))
        exponent = int(input("Enter exponent: "))
        print("Result:", exponentiate(base, exponent))

    elif choice == "R":  # Remainder
        num1 = int(input("\nEnter dividend: "))
        num2 = int(input("Enter divisor: "))
        result = remainder(num1, num2)
        if result is not None:
            print("Result:", result)

    elif choice == "F":  # Summation
        start = int(input("\nEnter first number: "))
        end = int(input("Enter second number: "))
        result = summation(start, end)
        if result is not None:
            print("Summation:", result)

    elif choice == "X":  # Exit the program
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a valid option.")