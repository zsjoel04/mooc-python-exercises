def longest_series_of_neighbours(list : list[int]) -> int:
    #[1, 2, 3, 10, 4, 5] teszt lista
    #1. lepes: atalakitani erre a formara
    #[[1, 2, 3], [10], [4,5]]

    # leellenorizzuk hogy ures e a tomb, mert csak akkor kell hozzaadni mind a kettot hogyha most kezdjuk az uj tmep tombot
    # [1, 2]
    # 2 3 [1, 2]
    # 3 10 [1, 2, 3] => mivel a 10 nem szomszedos ezert nullazunk
    # 10 4 [] nem
    collector_list = []
    temp_list = []
    for i in range(len(list) - 1):
        current = list[i]
        next = list[i+1]
        if len(temp_list) == 0:
            temp_list.append(current)
        if current + 1 == next or current - 1 == next:
            # ha szomszedosak
            temp_list.append(next)
        else:
            #nem szomszedosak
            collector_list.append(temp_list)
            temp_list = []
    collector_list.append(temp_list)
    #2. lepes: atalakitani csak a hosszakra
    #[len([1, 2, 3]), len([10]), len([4,5])]
    #[3, 1, 2]
    len_list = []
    for i in collector_list:
        len_list.append(len(i))
    #3. lepes: megkeresni a legnagyobbat a listabol
    max_len = max(len_list)
    return max_len

if __name__ =="__main__":
    my_list = [1, 2, 3, 10, 4, 5]
    print(longest_series_of_neighbours(my_list))