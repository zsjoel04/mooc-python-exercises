

word = input("")
lenght = len(word)
a = (14 - int(lenght/2))
b = a-1
if lenght % 2 == 1:
    print("*" * 30)
    print("*" + " " * a + word + " " * b + "*")
    print("*" * 30)
else:
    print("*" * 30)
    print("*" + " " * a + word + " " * a + "*")
    print("*" * 30)  

