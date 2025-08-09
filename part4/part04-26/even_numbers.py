def even_numbers(list_of_int : list[int]) -> list[int]:
    list_upgraded = []
    for i in list_of_int:
        if i % 2 == 0:
            list_upgraded.append(i)
    return(list_upgraded)
        

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 9, 1, 3, 6]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)