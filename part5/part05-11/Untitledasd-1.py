def asd(my_list, num1, num2, num3):
    new_list = my_list[:]
    new_list[num1][num2] = num3
    

    print(my_list)
    print(new_list)

my_list = [[1, 2, 3, 4],[2, 6, 7, 8]]

asd(my_list, 1, 2, 234)