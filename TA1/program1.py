# Prompt the user to enter a string and analyze the string to determine the # of vowels, consonants, spaces, and other characters
input_string = input("\n---- Please enter a string to analyze: ")
print("\nAnalyzing the input string...")

# Initialize the counters
vowelsCount = 0 # for counting the number of vowels
consonantsCount = 0 # for counting the number of consonants
spacesCount = 0 # for counting the number of spaces
otherChar = 0 # for counting the number of other characters such as numbers and special characters

vowels = "aeiouAEIOU" # list of vowels (uppercase and lowercase)

# loop
for char in input_string:
    if char.isalpha(): # check if the character is an alphabet
        if char in vowels: # check if the character is in the list of vowels
            vowelsCount += 1
        else:
            consonantsCount += 1
    elif char.isspace(): # check if the character is a space
        spacesCount += 1
    else:
        otherChar += 1

# Output the analysis
print("\n\n┌──         ANALYSIS OF THE INPUT STRING        ──┐\n")
print("\t   Number of vowels:", vowelsCount)
print("\t   Number of consonants:", consonantsCount)
print("\t   Number of spaces:", spacesCount)
print("\t   Number of other characters:", otherChar)
print("\n└──                                             ──┘")