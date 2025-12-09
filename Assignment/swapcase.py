word = input("Enter a word:")

empty_str = ''
for ch in word:
    code = ord(ch)
    if 65<= code <= 90:
        convert_lower_num = code + 32
        convert_lower_char = chr(convert_lower_num)
        empty_str+=convert_lower_char
    else:
        convert_upper_num = code - 32
        convert_upper_char = chr(convert_upper_num)
        empty_str+=convert_upper_char
print(empty_str)