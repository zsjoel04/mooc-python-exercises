name1 = input("Name: ")
age1 = int(input("Age: "))

name2 = input("Name: ")
age2 = int(input("Age: "))

if age1 < age2:
    print(f"The elder is {name2}")
elif age1 > age2:
    print(f"the elder is {name1}")

else:
    print(f"{name1} and {name2} are the same age")