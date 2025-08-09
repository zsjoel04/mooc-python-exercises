def invert(dictionary: dict) -> dict:
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key
    dictionary.clear()
    for key, value in new_dict.items():
        dictionary[key] = value



if __name__ =="__main__":
    s = {1: 10, 2: 20, 3: 30}
    invert(s)
    print(s)
