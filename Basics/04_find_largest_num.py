# Find the largest number among three numbers.

num1 = 15555
num2 = 333333333
num3 = 888

# Sol1
if num1 > num2 and num1 > num3:
    print(f"{num1} is largest")
elif num2> num3 and num2 > num1:
    print(f"{num2} is largest")
elif num3> num2 and num3> num1:
    print(f"{num3} is largest")
    
#Sol2
