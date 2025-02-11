try:
    file = open('numbers.txt', 'r')
    line_count = 1
    line = file.readline()
    
    title = "Check if a number is a palindrome.\n"
    centered_title = title.center(80)
    print(centered_title)
    
    while line != '':
        numbers = list(map(int, line.strip().split(",")))
        total_sum = sum(numbers)
        
        if str(total_sum) == str(total_sum)[::-1]:
            palindrome_status = "Palindrome"
        else:
            palindrome_status = "Not Palindrome"
            
        print(f"""Line {line_count}: 
        List of numbers: {line.strip()}
        Sum: {total_sum}
        Palindrome Status: {palindrome_status}\n""")
        
        line_count += 1
        line = file.readline()
    
    file.close()

except FileNotFoundError:
    print("The file 'numbers.txt' does not exist.")