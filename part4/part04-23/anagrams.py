

def anagrams(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    return False











if __name__ == "__main__":
    print(anagrams("tame", "meta"))