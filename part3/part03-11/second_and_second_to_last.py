word = input("")
a = word[1]
b = word[-2]
if a == b:
    print(f"The second and the second to last characters are {a}")
else:
    print(f"The second and the second to last characters are different")