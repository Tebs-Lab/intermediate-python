words = [
    'apple',
    'soda',
    'car',
    'intrepid',
    'water',
    'buffalo',
    'tepid',
    'enemy',
    'salvo'
]

# Use a list comprehension to generate a list that has the same words, but in all capital letters.
capitalized = [word.upper() for word in words]
print(capitalized)

# Use a list comprehension to generate a list that only has the words which start with a vowel.
vowel_starters = [word for word in words if word[0] in 'aeiou']
print(vowel_starters)

# Use a dictionary comprehension to map the words (as keys) to the length of the word (as values)
lengths = {word: len(word) for word in words}
print(lengths)