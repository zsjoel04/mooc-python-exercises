#import string




def dot_checker(word: str, search_term: str):
    new_list = []
    #alphabet = [letter for letter in string.ascii_lowercase]
    if len(search_term) == len(word):
        for i in range(len(search_term)):
            if search_term[i] == word[i]:
                new_list.append(word[i])
            elif search_term[i] == ".":# and word[i] in alphabet:
                new_list.append(word[i])
    result = "".join(new_list)
    if not result == "":
        if_true = word == result
        if if_true: 
            return result

# my_word = "asgadg"
# term = "ca."
# print(dot_checker(my_word, term))
    

def star_checker(word : str, search_term : str):
    length = len(search_term)
    if search_term[-1] == "*":
        result = search_term[:length - 1] == word[:length - 1]
        if result == True:
            return word
    elif search_term[0] == "*":
        my_len = len(word) - (length -1)
        result = word[my_len:] == search_term[1:]
        if result == True:
            return word
 
# my_word = "provokes"
# term = "*vokes"
# print(star_checker(my_word, term))
    

def find_words(search_term: str):
    parts = []
    with open("words.txt") as words:
    # words = ["cat", "buzi", "car", "california", "fdhgsdfhth"]
        for word in words:
            word = word.strip()
            if "." in search_term:
                result = dot_checker(word, search_term)
            elif "*" in search_term:
                result = star_checker(word, search_term)
            elif word == search_term:
                result = word
            else:
                result = None
            if result != None:
                parts.append(result)
    return parts
        



if __name__ == "__main__":
    print(word_search("*okes*"))
        




# def word_search(search_term: str):
#     with open("words.txt") as file:
#         words = [line.strip() for line in file]

#     matches = []

#     for word in words:
#         if matches_search(word, search_term):
#             matches.append(word)

#     return matches

# def matches_search(word: str, search_term: str):
#     Here manually handle "." and "*"
#     if "*" in search_term:
#         parts = search_term.split("*")
#         if len(parts) == 2:
#             start, end = parts
#             return word.startswith(start) and word.endswith(end) and len(word) >= len(start) + len(end)
#     elif "." in search_term:
#         if len(word) != len(search_term):
#             return False
#         for i in range(len(word)):
#             if search_term[i] != "." and search_term[i] != word[i]:
#                 return False
#         return True
#     else:
#         return word == search_term