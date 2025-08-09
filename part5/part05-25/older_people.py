def older_people(people: list, year: int):
    new_list = []
    for i in range(len(people)):
        if people[i][1] < year:
            new_list.append(people[i][0])
    return new_list


