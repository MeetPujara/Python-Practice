word = input("Enter word:")
alpha = True

for ch in word:
    code = ord(ch)
    if not (65 <= code <= 90) and not(97 <= code <= 122):
        alpha = False 

if alpha:
    print(f"{word} have alphabets")
else:
    print(f"{word} does not have alphabets")