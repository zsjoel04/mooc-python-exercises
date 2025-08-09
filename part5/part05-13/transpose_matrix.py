def transpose(matrix: list):
    full_list = []
    new_list = []
    index = 0
    while True:
        for i in range(len(matrix)):
            new_list.append(matrix[i][index])
        full_list.append(new_list)
        new_list = []
        index += 1
        if index == len(matrix):
            matrix[:] = full_list
            break




if __name__ == "__main__":
    my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(my_matrix)
    print(my_matrix)