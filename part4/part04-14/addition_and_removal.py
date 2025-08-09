my_list = []
number = 1
print(f"The list is now {my_list}")
operation = input("a(d)d, (r)emove or e(x)it: ")

while True:
    if operation == "d":
        my_list.append(number)
        number += 1
        print(f"The list is now {my_list}")
        operation = input("a(d)d, (r)emove or e(x)it: ")
        continue
    if operation == "r":
        my_list.pop(-1)
        number -= 1
        print(f"The list is now {my_list}")
        operation = input("a(d)d, (r)emove or e(x)it: ")
        continue
    if operation == "x":
        print("Bye!")
        break


