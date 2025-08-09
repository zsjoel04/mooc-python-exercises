sentence = input("Please type in a sentence: ")


while True:
    x = " " in sentence
    if x == False:
        print(sentence[0])
        break
    else:
        print(sentence[0])
        space = sentence.find(" ")          # The index of the space
        letter = space + 1                  # The index of the first letter
        sentence = sentence[letter:]

    if x == False:
        break
    