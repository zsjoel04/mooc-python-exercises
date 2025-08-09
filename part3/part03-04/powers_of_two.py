limit = int(input())
num = 2
base = 2
exp = -1
while num <= limit:
    exp += 1 
    num = base**exp
    if num <= limit:
        print(num)




# limit = int(input())
# num = 1
# while num <= limit:
#     print(num)
#     num *= 2