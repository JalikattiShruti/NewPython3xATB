# Count vowels and consonants in a String

# Define vowels
vowels = "aeiouAEIOU"

# input
input_str = input("Enter a string: ")

vowel_count = sum(1 for char in input_str if char in vowels)
consonant_count = sum(1 for char in input_str if char.isalpha() and char not in vowels)

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
