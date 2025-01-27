input_string = input("\n---- Please enter a string to analyze: ")
print("\nAnalyzing the input string...")

vowelsCount = 0 
consonantsCount = 0 
spacesCount = 0 
otherChar = 0 

vowels = "aeiouAEIOU" 

for char in input_string:
    if char.isalpha():
        if char in vowels:
            vowelsCount += 1
        else:
            consonantsCount += 1
    elif char.isspace():
        spacesCount += 1
    else:
        otherChar += 1

print("\n\n┌──         ANALYSIS OF THE INPUT STRING        ──┐\n")
print("\t   Number of vowels:", vowelsCount)
print("\t   Number of consonants:", consonantsCount)
print("\t   Number of spaces:", spacesCount)
print("\t   Number of other characters:", otherChar)
print("\n└──                                             ──┘")