def create_tuple(x: int, y: int, z: int):
    my_list = [x, y, z]
    mini = min(my_list)
    maxi = max(my_list)
    my_sum = x + y + z
    my_tuple = (mini, maxi, my_sum)
    return(my_tuple)
    





if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
