print("\n---- Part a: Right-aligned triangle")
n = 5 
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for num in range(1, row + 1):
        print(num, end="")
    print()  # move to the next line

print("\n---- Part b: Pattern")
skip = 1  
row = 1  
while row <= 5: 
    count = 1
    while count <= skip:
        print(skip, end="")
        count += 1
    print() # move to the next line
    skip += 2
    row += 1 
print()