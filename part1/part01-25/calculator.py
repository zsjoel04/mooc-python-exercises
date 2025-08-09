num1 = int(input())
num2 = int(input())
multi_result = num1 * num2
add_result = num1 + num2
subtr_result = num1 - num2


operation = input()

if operation == "multiply":
    print(f"{num1} * {num2} = {multi_result}")
elif operation == "add":
    print(f"{num1} + {num2} = {add_result}")
elif operation == "subtract":
    print(f"{num1} - {num2} = {subtr_result}")

