a = 1
fact = 1
num = 10
while not num <= 0:
    num = int(input())
    if num <= 0:
        print("Thanks and bye!")
        break
    for i in range(num):
        fact *= a
        a += 1
    print(f"The factorial of the number {num} is {fact}")
    fact = 1
    a = 1
    