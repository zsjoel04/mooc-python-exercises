def shortest(list : list[str]) -> list[str]:
    shortest = list[0]
    for i in range(len(list)):
        if len(shortest) > len(list[i]):
            shortest = list[i]
    return shortest






if __name__ == "__main__":
    my_list = ['Alan', 'Susan', 'Seymour', 'Kim', 'Susan']
    result = shortest(my_list)
    print(result)