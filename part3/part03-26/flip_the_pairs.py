num = int(input())
a = 2
b = 1
while True:
    if num == 1:
        print(1)
        break
    print(a)
    print(b)
    a += 2
    b += 2
    if num % 2 == 1:
        if a > num and b <= num:
            print(b)
            break
        elif a <= num and b > num:
            print(a)
            break
    if a > num or b > num:
        break


