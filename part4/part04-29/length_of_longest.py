
def length_of_longest(list : list[str]) -> int:
    longest = list[0]
    for i in range(len(list)):
        if len(longest) < len(list[i]):
            longest = list[i]
    return len(longest)








if __name__ == "__main__":
    my_list = ['Alan', 'Grace', 'Frances', 'Kim', 'Susan']
    result = length_of_longest(my_list)
    print(result)