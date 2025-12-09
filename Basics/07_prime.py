num = 3

for i in range(2,num):
    if num % i == 0:
        print(f"{num} is Not Prime")
        break
    else:
        print(f"{num} is Prime")    
        break