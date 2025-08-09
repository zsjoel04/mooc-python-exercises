num = int(input())
num_change = num
b = 1
step = 0
while True:
    print(b)
    b += 1
    step += 1
    if step == num:
        break
    print(num_change)
    num_change -= 1
    step += 1
    if step == num:
        break
        





