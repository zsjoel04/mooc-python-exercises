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

if __name__ =="__main__":
    sudoku = [
    [ 9, 0, 1, 0, 8, 0, 3, 0, 1 ],
    [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 2, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 8, 6 ],
    [ 3, 0, 1, 0, 0, 0, 0, 0, 1 ],
    [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],
    ]
    column_correct(sudoku, 0)

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))