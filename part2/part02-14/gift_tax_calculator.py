gift = int(input("Value of gift: "))

if 5000 <= gift <= 25000:
    tax = ((gift - 5000) * 0.08) + 100
    print(f"Amount of tax: {tax}")
elif 25001 <= gift <= 55000:
    tax = ((gift - 25000) * 0.1) + 1700
    print(f"Amount of tax: {tax}")
elif 55001 <= gift <= 200000:
    tax = ((gift - 55000) * 0.12) + 4700
    print(f"Amount of tax: {tax}")
elif  200001 <= gift <= 1000000:
    tax = ((gift - 200000) * 0.15) + 22100
    print(f"Amount of tax: {tax}")
elif 1000001 <= gift:
    tax = ((gift - 1000000) * 0.17) + 142100
    print(f"Amount of tax: {tax}")
else:
    print("No tax!")
