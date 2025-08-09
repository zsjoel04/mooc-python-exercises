def matrix_sum():
    sum = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            sum += mymatrix_sum(row_splitter(line))
    return sum

def matrix_max():
    max = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            for i in row_splitter(line):
                if int(i) > max:
                    max = int(i)
    return(max)
                
def row_sums():
    my_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            my_list.append(mymatrix_sum(row_splitter(line)))
    return my_list


# HELPER FUNCTIONS(FROM HERE)
def mymatrix_sum(my_list):
    sum = 0
    for i in my_list:
        sum += int(i)
    return sum

def row_splitter(my_line : str):
    my_line = my_line.replace("\n", "")
    lines_split = my_line.split(",")
    return lines_split
# HELPER FUNCTIONS(UNTIL HERE)

if __name__ == "__main__":
    print(row_sums())