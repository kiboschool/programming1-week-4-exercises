# Write your code below
# Create an empty list to store the words
words = []

# Ask the user for 5 words
for i in range(5):
    word = input("Enter a word: ")
    words.append(word)  # Add each word to the list

# Assume the first word is the longest to start
longest_word = words[0]

# Loop through the list to find the longest word
for word in words:
    if len(word) > len(longest_word):
        longest_word = word  # Update if a longer word is found

# Print the longest word
print(longest_word)
