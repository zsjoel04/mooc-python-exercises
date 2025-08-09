def dict_of_numbers():
    my_dict = {}
    my_list = []
    zero = my_dict[0] = "zero"
    one = my_dict[1] = "one"
    two = my_dict[2] = "two"
    three = my_dict[3] = "three"
    four = my_dict[4] = "four"
    five = my_dict[5] = "five"
    six = my_dict[6] = "six"
    seven = my_dict[7] = "seven"
    eight = my_dict[8] = "eight"
    nine = my_dict[9] = "nine"
    ten = my_dict[10] = "ten"
    my_list.append(one)
    my_list.append(two)
    my_list.append(three)
    my_list.append(four)
    my_list.append(five)
    my_list.append(six)
    my_list.append(seven)
    my_list.append(eight)
    my_list.append(nine)
    my_dict[11] = "eleven"
    my_dict[12] = "twelve"
    my_dict[13] = "thirteen"
    my_dict[14] = "fourteen"
    my_dict[15] = "fifteen"
    my_dict[16] = "sixteen"
    my_dict[17] = "seventeen"
    my_dict[18] = "eighteen"
    my_dict[19] = "nineteen"
    my_dict[20] = "twenty"
    twenty = "twenty"
    thirty = "thirty"
    forty = "forty"
    fifty = "fifty"
    sixty = "sixty"
    seventy = "seventy"
    eighty = "eighty"
    ninety = "ninety"
    my_list2 = []
    my_list2.append(twenty)
    my_list2.append(thirty)
    my_list2.append(forty)
    my_list2.append(fifty)
    my_list2.append(sixty)
    my_list2.append(seventy)
    my_list2.append(eighty)
    my_list2.append(ninety)
    index = 0
    num1 = 21
    num2 = 30
    for i in range(len(my_list2)):
        for item in range(num1, num2):
            my_dict[item] = f"{my_list2[i] + "-" + my_list[index]}"
            index += 1
        index = 0
        if not i > 6:
            my_dict[num2] = my_list2[i + 1]
        num1 += 10
        num2 += 10
    return my_dict


if __name__ == "__main__":
    print(dict_of_numbers())
    numbers = dict_of_numbers()
    print(numbers[3])
    print(numbers[40])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])