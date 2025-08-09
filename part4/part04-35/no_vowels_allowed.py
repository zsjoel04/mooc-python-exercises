def no_vowels(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "u" or string[i] == "i" or string[i] == "o" or string[i] == "a" or string[i] == "e":
            continue
        new_string += string[i]
    return new_string


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))