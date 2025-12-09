# capitalize(), isalnum(), isalpha(), islower(), swapcase(), replace(), strip()
# Set:difference(), intersection(), isdisjoint(), issubset(), symmetric_difference(), union()

word = input("Enter a word: ")
first_char = word[0]
remaining_words = word[1:]

num = ord(first_char)

if 97 <= num <= 122:
    upper_num = num - 32
    upper_char = chr(upper_num)
else:
    upper_char = first_char

result = upper_char + remaining_words
print(result)