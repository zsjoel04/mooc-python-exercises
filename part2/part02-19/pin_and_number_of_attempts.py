attempts = 0


while True:
    pin = input("PIN: ")
    attempts += 1
    if attempts == 1:
        if pin == "4321":
            print("Correct! It only took you one single attempt!")
            break
    elif pin == "4321":
        print(f"Correct! It took you {attempts} attempts")
        break
    
    print("Wrong")
    