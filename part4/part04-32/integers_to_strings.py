
def formatted(list: list[float]) -> list[str]:
    new_list = []
    for i in list:
        new_list.append(str(f"{i:.2f}"))
    return(new_list)







if __name__ == "__main__":
    my_list = ([0.123, 1.23, 0.0234])
    new_list = formatted(my_list)
    print(new_list)