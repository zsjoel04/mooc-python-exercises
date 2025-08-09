def spell_checker(my_sentence : str) -> str:
    my_list = []
    my_sentence = my_sentence.split(" ")
    a = 0
    with open("wordlist.txt") as new_file:
        new_list = []
        new_file_list = [line.strip() for line in new_file]
        for word in my_sentence:
            if word.lower() in new_file_list:
                new_list.append(word)
            else:
                new_list.append(f"*{word}*")
    return new_list
                
def convert_into_str(my_list : list) -> str:
    new_str = ""
    for word in my_list:
        new_str += f"{word} "
    return new_str

def printout():
    sentence = input()
    result = spell_checker(sentence)
    print(convert_into_str(result))

printout()

