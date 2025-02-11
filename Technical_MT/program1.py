try:
    # Open the file 'numbers.txt' in read mode
    file = open('numbers.txt', 'r')
    line_count = 1
    line = file.readline()
    
    title = "Check if a number is a palindrome.\n"
    centered_title = title.center(80)
    print(centered_title)
    
    # Read the file line by line using a while loop
    while line != '':
        numbers = list(map(int, line.strip().split(","))) # Convert the string of numbers to a list of integers
        total_sum = sum(numbers) # Calculate the sum of the numbers in the list
        
        # Check if the sum is a palindrome
        if str(total_sum) == str(total_sum)[::-1]:
            palindrome_status = "Palindrome"
        else:
            palindrome_status = "Not Palindrome"
        
        # Print the line number, list of numbers, sum, and palindrome status   
        print(f"""Line {line_count}: 
        List of numbers: {line.strip()}
        Sum: {total_sum}
        Palindrome Status: {palindrome_status}\n""")
        
        # Read the next line
        line_count += 1
        line = file.readline()
    
    file.close()

# Handle the FileNotFoundError exception
except FileNotFoundError:
    print("The file 'numbers.txt' does not exist.")