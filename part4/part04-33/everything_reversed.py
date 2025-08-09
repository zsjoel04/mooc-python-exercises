

def items_reversed(list : list[str]) -> list[str]:
    new_list1 = []
    for i in range(len(list)):
        new_list1.append(list[-i - 1])
    return new_list1

def everything_reversed(list):
    words_reversed = []
    for i in range(len(list)):
        words_reversed.append(list[i][::-1])
    return items_reversed(words_reversed)




if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
