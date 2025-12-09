word = input("Enter word: ")
alnum = True
for ch in word:
    code = ord(ch)
    # print(code)
    if not (48 <= code <= 57) and not (65 <= code <= 90) and not (97 <= code <= 122):
        alnum = False

if alnum:
    print(f"{word} is alphanumeric")
else:
    print(f"{word} is not alphanumeric")

# (97 <= code <= 122) -> ((code >= 97) and (code <= 122))