def row_correct(sudoku: list, row_no: int):
    my_list = sudoku[row_no]
    return match_check(my_list)

def match_check(list):
    for square in range(len(list)):
        current = list[square]
        new_list = list[square + 1:]
        for i in new_list:
            if i != 0:
                if i == current:
                    return False
    return True



def column_correct(sudoku: list, column_no: int):
    new_list = []
    for number in sudoku:
        new_list.append(number[column_no])
    result = my_list(new_list)
    return result

def my_list(lista):
    for i in range(len(lista)):
        saved = lista[i]
        my_new_list = lista[i + 1:]
        for number in my_new_list:
            if number != 0:
                if number == saved:
                    return False
    return True



def block_correct(sudoku: list, row_no: int, column_no: int):
    lista = block_finder(sudoku, row_no, column_no)
    for i in range(len(lista)):
        count_a = lista.count(lista[i])
        if count_a > 1:
            return False
    return True


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

def sudoku_grid_correct(sudoku: list):
    the_list0 = [0, 3, 6] 
    the_list1 = [1, 4, 7]
    index_1 = 0
    index_2 = 0
    for i in range(len(sudoku)):
        result1 = row_correct(sudoku, i)
        result2 = column_correct(sudoku, i)
        result3 = block_correct(sudoku, index_1, index_2)
        if i > 2 and i < 6:
            index_1 = 3
        elif i > 5:
            index_1 = 6
        
        if i in the_list0:
            index_2 = 0
        if i in the_list1:
            index_2 = 3
        else:
            index_2 = 6  
        if result1 == False or result2 == False or result3 == False:
            return False
    return True



if __name__ =="__main__":
    sudoku1 = [
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
    print(sudoku_grid_correct(sudoku1))
    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))