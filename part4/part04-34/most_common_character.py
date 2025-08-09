

def most_common_character(string):
    count_result = 0
    result = ""
    for i in range(len(string)):
        count = string.count(string[i])
        if count > count_result:
            count_result = count
            result = string[i]
    return result








if __name__ == "__main__":
    print(most_common_character("aaabb"))
