# Follow the instructions in the tab to the right
# Write your code below
words = []
for i in range(5):
  user_input = input('Enter a word: ')
  words.append(user_input)

longest = ""
for word in words:
  if len(word) > len(longest):
    longest = word

print(longest)
