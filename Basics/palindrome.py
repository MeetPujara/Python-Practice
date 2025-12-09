num = 121
a = num 
rev = 0


while a > 0:
    ld = a %10
    rev = (rev * 10) + ld
    a = a // 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")