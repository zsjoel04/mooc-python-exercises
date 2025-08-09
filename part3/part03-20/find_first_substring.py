word = input("Please type in a word:")
caracter = input("Please type in a character:")
value = caracter in word
a = word.find(caracter)


lenght = len(word)
c = len(word[a:])


if value == True:
    if c < 3:
        print("")
    else:
        print(word[a:a+3])