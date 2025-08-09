
def first_word(sentence):
    space1 = sentence.find(" ")
    return(sentence[0:space1])

def second_word(sentence):
    sentence = sentence[len(first_word(sentence)) +1 :]
    space2 = sentence.find(" ")
    if space2 == -1:
        return sentence
    return sentence[0 : space2]

def last_word(sentence):
    a = sentence[::-1]
    space3 = a.find(" ")
    b = (a[0:space3])
    c = b[::-1]
    return c
   

if __name__ == "__main__":
    sentence = "sikerulni fog"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))