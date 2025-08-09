import math as m

number = int(input("How many students on the course?"))
group_size = int(input("Desired group size? "))


group_number = number / group_size
group_number = m.ceil(group_number)

print(f"Number of groups formed: {group_number} ")