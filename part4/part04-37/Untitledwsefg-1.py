def longest_series_of_neighbours(list : list[int]) -> int:
    numbers_result = numbers(list)      #numbers funknio eredmenye [a, b]
    list_cut = list[numbers_result[1]:] #eredeti lista levagott resze
    lenght = numbers_result[1]          
    result = numbers_result[0]
    while True:
        if lenght > len(list):
            return result
        numbers_result = numbers(list_cut)
        list_cut = list_cut[numbers_result[1]:]
        if result < numbers_result[0]:
            result = numbers_result[0]
        if numbers_result[0] == 1 or numbers_result[1] == -1:
            return result
        lenght += numbers_result[1]
        

def numbers(list):
    list_result = []
    index = 1
    neighbours = 1
    for i in list:
        if index >= len(list):
            return [neighbours, -1]
        if i + 1 == list[index] or i-1 == list[index]:
            neighbours += 1
            index += 1
        else:
            if neighbours >= 2:
                list_result.append(neighbours)
                list_result.append(index)
                return list_result
            index += 1
            
            
if __name__ =="__main__":
    my_list = [19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))