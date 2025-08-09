pw = input("Password: ")

while True:
    pw_repeat = input("Repeat password: ")
    if pw_repeat == pw:
        break
    print("They do not match!")
print("User account created!")