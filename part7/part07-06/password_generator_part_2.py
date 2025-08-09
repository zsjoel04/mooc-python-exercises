import string
import random

def numbers(max_len):
    nums = [num for num in string.digits]
    random_num = random.randint(1, max_len)
    result = random.sample(nums, random_num)
    return result    

def chars(max_len):
    chars = list("!?=+-()#")
    random_num = random.randint(1, max_len)
    result = random.sample(chars, random_num)
    return result

def generate_strong_password(length, if_nums, if_chars):
    letters = [letter for letter in string.ascii_lowercase]
    result = []
    if if_nums == True:
        result += numbers(length - 1)
        length -= len(result)
    if if_chars == True:
        result += chars(length - 1)
        length -= len(chars(length - 1))
    if not length == 1:
        result += random.sample(letters, length)
    elif length == 1:
        result += random.choice(letters)
    return result

print(generate_strong_password(8, True, True))




