
def palindromes(pal:str) -> bool:
    reversed_pal = pal[::-1]
    return reversed_pal == pal

def search_palindrome():
    while True:
        word = input("")
        if palindromes(word) == True:
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")

        
search_palindrome()

