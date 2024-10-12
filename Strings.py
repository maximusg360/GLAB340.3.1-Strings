word = input("Please enter a word: ")

print("Length of word:", len(word))

# Convert to uppercase and lowercase
print("To uppercase:", word.upper())
print("To lowercase:", word.lower())

# Count how many times a letter appears in a word
letter = input("Please enter a letter: ")
print(f" The '{letter}' appears {word.count(letter)} times")

# How many times a substring appears in the word.
substring = input("Please enter a substring: ")
print(f"The '{substring}' appears {word.count(substring)} time(s)")

# Reversing the word and print it out
reverse_word = word.split()[::-1]
print("Reversed word:", reverse_word)

# Slice the word and print the result
start_index = int(input("Please enter a starting index: "))
end_index = int(input("Please enter an ending index: "))
sliced_word = word[start_index:end_index]
print("Sliced word:", sliced_word)

# Replacingthe first occurrence of a character with another character.
character_to_replace = input("Please enter a character to replace: ")
replacement_character = input("Enter the replacement character: ")
new_word = word.replace(character_to_replace, replacement_character, 1)
print("Replaced:", new_word)

# Concatenate an original word with a second word
second_word = input("Please enter a second word: ")
concatenated_word = word + second_word
print("Concatenated words:", concatenated_word)

# Check for palindrome and valid identifier
is_palindrome = word == reverse_word
is_valid_identifier = word.isidentifier()

print("Is a palindrome?", is_palindrome)
print("Is a valid Python identifier?", is_valid_identifier)