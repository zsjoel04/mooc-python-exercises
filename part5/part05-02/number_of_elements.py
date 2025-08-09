
def count_matching_elements(my_matrix: list, element: int):
    result = 0
    for i in range(len(my_matrix)):
        my_list = my_matrix[i]
        searching_for = element
        result += in_matrix_elements(my_list, searching_for)
    return result



def in_matrix_elements(my_list, searching_for):
    matching = 0
    for i in my_list:
        if i == searching_for:
            matching += 1
    result = matching     
    return result

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))