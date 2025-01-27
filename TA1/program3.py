# Prints a right-aligned triangle using loops
print("\n---- Part a: Right-aligned triangle")
n = 5 # number of rows
for row in range(1, n + 1):
    for space in range(n - row): # print spaces
        print(" ", end="")
    for num in range(1, row + 1): # print numbers
        print(num, end="")
    print()  # move to the next line

# Prints a pattern using loops
print("\n---- Part b: Pattern")
skip = 1  # number of digits to skip
row = 1  # number of rows
while row <= 5: 
    count = 1 # initialize the counter
    while count <= skip: # loop to print the numbers
        print(skip, end="")
        count += 1
    print() 
    skip += 2 # increment the number of digits to skip
    row += 1 # increment the number of rows
print()