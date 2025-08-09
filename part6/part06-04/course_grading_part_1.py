student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
def one_iteration(name_csv):
    my_dict = {}
    with open(name_csv) as new_file:
        for line in new_file:
            parts = line.split(";")
            if not parts[0] == "id":
                my_dict[parts[0]] = (parts[1], parts[2].strip())
    return my_dict

def my_iteration(exercises_csv):
    my_dict = {}
    with open(exercises_csv) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if not parts[0] == "id":
                lista = []
                result = 0                
                for i in parts[1:]:
                    result += int(i)
                my_dict[parts[0]] = result
    return my_dict


def printout():
    name = one_iteration(student_info)
    exercises = my_iteration(exercise_data)
    for key, value in name.items():
        id = key
        print(f"{name[id][0]} {name[id][1]} {exercises[id]}")

printout()


# {'12345678': ('pekka', 'peloton'), '12345687': ('jaana', 'javanainen'), '12345699': ('liisa', 'virtanen')}
# {'12345678': 21, '12345687': 27, '12345699': 35}