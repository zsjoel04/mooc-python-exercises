

def sum(list):
    index = 0
    sum = 0
    for i in list:
        sum += list[index] 
        index += 1
    return sum

def mean(list):
    return sum(list) / len(list)

   


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)