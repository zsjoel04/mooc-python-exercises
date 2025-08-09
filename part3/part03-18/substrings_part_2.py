word = input("")
index = -1
lenght = len(word)
for i in range(lenght-1):
    if index == -1:
        print(word[-1])
    index -= 1
    print(word[index:])