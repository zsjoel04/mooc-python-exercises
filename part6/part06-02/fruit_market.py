def read_fruits():
    fruits_dict = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            new_list = line.split(";")
            new_list[1]
            fruits_dict[new_list[0]] = float(new_list[1])
    return(fruits_dict)

