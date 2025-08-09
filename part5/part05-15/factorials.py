

def factorials(n: int):
    my_dict = {}
    for i in range(1, n + 1):
        if n == 1:
            my_dict[1] = fact(1)
        my_dict[i] = fact(i)
    return my_dict


def fact(num : int):
    result = 1
    for i in range(1 , num + 1):
        result *= i
    return result


