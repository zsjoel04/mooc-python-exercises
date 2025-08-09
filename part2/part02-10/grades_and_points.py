points = int(input("How many points [0-100]: "))
if points < 0 or points > 100:
    print("impossible!")
elif 0 < points <= 49:
    print("fail")
elif 49 < points <= 59:
    print("Grade: 1")
elif 59 < points <= 69:
    print("Grade: 2")
elif 69 < points <= 79:
    print("Grade: 3")
elif 79 < points <= 89:
    print("Grade: 4")
elif 89 < points <= 100:
    print("Grade: 5")