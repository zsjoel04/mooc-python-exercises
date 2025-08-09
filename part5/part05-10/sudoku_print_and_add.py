

def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        for x in range(len(sudoku)):
            if sudoku[i][x] != 0:
                print(sudoku[i][x], end = " ")
                if (x + 1) % 3 == 0:
                    print(" ", end = "")
            elif sudoku[i][x] == 0:
                print("_", end = " ")
                if (x + 1) % 3 == 0:
                    print(" ", end = "")
        print()
        if (i + 1) % 3 == 0:
            print()





def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    return sudoku
if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)