

def no_shouting(list : list[str]) -> list[str]:
    new_list = []
    for i in range(len(list)):
        if not list[i].isupper():
            new_list.append(list[i])
    return new_list
    



if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    prined_list = no_shouting(my_list)
    print(prined_list)