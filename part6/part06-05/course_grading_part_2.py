student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
my_points = input("points: ")

def lis_of_num(a, b):
    lista = []
    for i in range(a, b):
        lista.append(i)
    return lista


def one_iteration(name_csv):        #id - name
    my_dict = {}
    with open(name_csv) as new_file:
        for line in new_file:
            parts = line.split(";")
            if not parts[0] == "id":
                my_dict[parts[0]] = (parts[1], parts[2].strip())
    return my_dict

def my_iteration(exercises_csv):        #id - exercises
    my_dict = {}
    with open(exercises_csv) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if not parts[0] == "id":
                result = 0                
                for i in parts[1:]:
                    result += int(i)
                my_dict[parts[0]] = result
    return my_dict

def printout():
    zero = lis_of_num(0,15)
    one = lis_of_num(15, 18)
    two = lis_of_num(18, 21)
    three = lis_of_num(21, 24)
    four = lis_of_num(24, 28)

    points = my_iteration(my_points)
    name = one_iteration(student_info)
    exercises = my_iteration(exercise_data)
    for key, value in name.items():
        final_points = exercises[key] / 40 * 10
        result = points[key] + int(final_points)
        if result in zero:
            result = 0
        elif result in one:
            result = 1
        elif result in two:
            result = 2
        elif result in three:
            result = 3
        elif result in four:
            result = 4
        else:
            result = 5
        print(f"{name[key][0]} {name[key][1]} {result}")


printout()
