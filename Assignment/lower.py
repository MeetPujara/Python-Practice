word = input("Enter a word: ")
lower = True

for ch in word:
    code = ord(ch)
    if 65 <= code <= 90:
        lower = False

if lower:
    print("Characters are in lowercase")
else:
    print("Characters are in uppercase")