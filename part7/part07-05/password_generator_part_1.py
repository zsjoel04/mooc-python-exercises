import string
from random import shuffle

def generate_password(length : int):
    abc = [letter for letter in string.ascii_lowercase]
    shuffle(abc)
    result = abc[:length]
    return "".join(result)

# print(generate_password(3)) 