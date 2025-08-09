num = 0
sum = 0
pos = 0
neg = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    numbers = int(input(""))
    if numbers == 0:  
        print(f"Numbers typed in {num}")    
        print(f"The sum of the numbers is {sum}")
        print(f"The mean of the numbers is {sum/num}")
        print(f"Positive numbers {pos}")
        print(f"Negative numbers {neg}")
        break
    if numbers < 0:
        neg += 1
    elif numbers:
        pos += 1
    num += 1
    sum += numbers