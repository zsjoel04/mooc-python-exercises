

def list_of_recipes(filename : str):
    list_recycle = []
    new_list = []
    with open(filename) as new_file:
        list_of_recipies = [line.strip() for line in new_file]
    for line in list_of_recipies:
        if not line == "":
            list_recycle.append(line)
        else:
            new_list.append(list_recycle)
            list_recycle = []
    new_list.append(list_recycle)
    return new_list


def search_by_name(filename: str, word: str):
    new_list = list_of_recipes(filename)
    result_list = []
    for my_word in new_list:
        if word in my_word[0].lower():
            result_list.append(my_word[0])
    return result_list

def search_by_time(filename: str, prep_time: int):
    new_list = list_of_recipes(filename)
    result_list = []
    for one_list in new_list:
        if int(one_list[1]) <= int(prep_time):
            result = f"{one_list[0]}, preparation time {one_list[1]} min"
            result_list.append(result)
    return result_list


def search_by_ingredient(filename: str, ingredient: str):
    new_list = list_of_recipes(filename)
    result_list = []
    recycle_list = []
    for one_list in new_list:
        result = ingredient_finder(one_list)
        for word in result:
            if ingredient in word:
                result = f"{one_list[0]}, preparation time {one_list[1]} min"
                result_list.append(result)
                continue
    return result_list

def ingredient_finder(ingredients : list) -> list:
    new_list = []
    for i in range(len(ingredients)):
        if i > 1:
            new_list.append(ingredients[i])
    return new_list
        


if __name__ == "__main__":
    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)