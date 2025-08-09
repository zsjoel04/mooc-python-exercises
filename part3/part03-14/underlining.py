end = ""
string = "a"
while not string == end:
    string = input("Please type in a string: ")
    print(string)
    length = len(string)
    print("-" * length)
