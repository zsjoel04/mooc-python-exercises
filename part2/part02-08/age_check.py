age = int(input("What is your age?"))
if age >= 5:                                        # 5-99
    print(f"Ok, you're {age} years old")
elif 0 <= age < 5:                                   # 0-4
    print("I suspect you can't write quite yet...")
else:                                               # 
    print("That must be a mistake")