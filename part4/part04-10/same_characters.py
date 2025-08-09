



def same_chars(string, num1, num2):
    length = len(string)
    if num1 > length - 1 or num2 > length - 1:
        return False
    if string[num1] == string[num2]:
        return True
    else:
        return False








if __name__ == "__main__":
    print(same_chars("coder", 1, 10))