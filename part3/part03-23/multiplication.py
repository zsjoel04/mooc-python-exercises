num = int(input("Please type in a number:"))
num1 = 1
num2 = 1
for i in range(num):
    while not num2 > num:
        result = num1 * num2
        print(f"{num1} x {num2} = {result}")
        num2 += 1
    num1 += 1
    num2 = 1



