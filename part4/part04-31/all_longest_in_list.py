
def all_the_longest(list : list[str]) -> list[str]:
    new_list = []
    longest = list[0]
    for i in range(len(list)):
        if len(longest) < len(list[i]):
            longest = list[i]
    new_list.append(longest)
    for i in range(len(list)):
        if len(longest) == len(list[i]) and longest != list[i]:
            new_list.append(list[i])
    return new_list
        



if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)