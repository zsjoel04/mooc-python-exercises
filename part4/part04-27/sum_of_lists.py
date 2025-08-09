def list_sum(list1 : list[int], list2 : list[int]) -> list[int]:
    index = 0
    new_list = []
    for i in list1:
        x = i + list2[index]
        new_list.append(x)
        index += 1
    return new_list


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))


