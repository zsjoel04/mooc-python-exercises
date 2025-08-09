
def block_correct(sudoku: list, row_no: int, column_no: int):
    lista = block_finder(sudoku, row_no, column_no)
    for i in range(len(lista)):
        count_a = lista.count(lista[i])
        if count_a > 1:
            return False
    return True

    # lista = block_finder(sudoku, row_no, column_no)
    # for x in range(len(lista)):
    #     result = one_iteration(lista)
    #     lista = lista[x + 1:]
    #     if result == False:
    #         return result
    # return result

# def one_iteration(list):
#     for i in range(len(list)):
#         if i > 0:
#             if list[0] == list[i]:
#                 return False  
#     return True
   


def block_finder(list : list, row : int, column : int) -> list:
    column_original = column
    new_list = []  
    for i in range(3):
        for x in range(3):
            if list[row][column] != 0:
                new_list.append(list[row][column]) 
            column += 1
        row += 1
        column = column_original
    return new_list



if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))