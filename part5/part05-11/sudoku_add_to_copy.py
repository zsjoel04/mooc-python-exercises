def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    list_copied = sudoku[:]
    two_d_list = sudoku[row_no]
    new_list = two_d_list[:]
    new_list[column_no] = number
    list_copied[row_no] = new_list
    return list_copied
    

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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print(sudoku)
    print()
    print("Copy:")
    print(grid_copy)

