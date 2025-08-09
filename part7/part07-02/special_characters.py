import string



def separate_characters(my_string: str):
    part1 = ""
    alpha = [letter for letter in string.ascii_letters]
    for caracter in my_string:
        if caracter in alpha:
            print(caracter)
            part1 = "".join(part1)
    
    print(part1)

my_string = "BGÉÁ őú Ooi"
separate_characters(my_string)