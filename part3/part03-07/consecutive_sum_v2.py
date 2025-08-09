limit =  int(input("Limit: "))
num = 1
sum = 0
calculation = ""
buzi = " + "
while not limit <= sum:
    calculation += f"{num}"

    sum += num 
    num += 1 
    
    if sum >= limit:
        calculation += f" = {sum}"
    else:
        calculation += buzi


print(f"The consecutive sum: {calculation}")

















# limit =  int(input("Limit: "))
# num = 1
# sum = 0
# calculation = ""
# buzi = " + "
# while not limit <= sum:
#     if num - sum < limit:
#         calculation += f"{num}{buzi}"
#     sum += num #10
#     num += 1 #5
    
#     if sum >= limit:
#         calculation += f" = {sum}"


# print(calculation)

















# limit =  int(input("Limit: "))
# num = 1
# sum = 0
# szamok = []
# while not limit <= sum:
#     sum += num #10
#     szamok.append(num)
#     num += 1 #5
# calculation = ""
# for i in szamok:
#     if not i == szamok[-1]:
#         calculation += f"{i} + "
#     else:
#         calculation += f"{szamok[-1]} = {sum}"

# print(f"The consecutive sum: {calculation}")

















# limit = int(input())
# num = 1
# sum = 0
# calculation = ""
# while not limit <= sum:
#     if limit - num > sum:
#         calculation += f"{num} + "
#     sum += num
#     num += 1
#     if limit <= sum:
#         calculation += f"{num} = {sum} "
# print(calculation)