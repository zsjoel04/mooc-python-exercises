name = input("Please tell me your name:")
Jerry = "Jerry"
portion = 5.9
if name == Jerry:
    print("Next please!")
else:
    cost = int(input("How many portions of soup?"))
    print(f"The total cost is {cost * portion}")
    print("Next please!")