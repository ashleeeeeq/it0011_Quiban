# List of words to exlude and get the statement from the user
excluded_words = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "to", "of"}
userInput = input("Enter a string statement: ")

# Split the statement into words and filter out excluded words
word_split = userInput.split()
filtered_words = []

# Filter out excluded words
for word in word_split:
    if word.lower() not in excluded_words:
        filtered_words.append(word)

# Count unique words in the filtered list
word_count = {}
for word in filtered_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
# Separate lowercase and uppercase words
lowercase_words = []
uppercase_words = []

for word in word_count:
    if word[0].islower():
        lowercase_words.append(word)
    else:
        uppercase_words.append(word)

# Sort each group alphabetically
lowercase_words.sort()
uppercase_words.sort()

# Display results and the total words filtered 
print("\n------------------------------------------------------------")
print("                       WORD COUNTER")
print("------------------------------------------------------------")

for word in lowercase_words + uppercase_words:  # Print lowercase first, then uppercase
    print("     ", word, " " * (20 - len(word)), "-          ", word_count[word])

print("\n     Total words filtered:             ", sum(word_count.values()))
print("------------------------------------------------------------")
