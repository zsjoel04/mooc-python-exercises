limit = int(input())
base = int(input())
num = base
exp = -1
while num <= limit:
    exp += 1
    num = base**exp
    if num <= limit:
        print(num)
