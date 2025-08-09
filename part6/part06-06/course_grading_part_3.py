if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    my_points = input("points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    my_points = "exam_points1.csv"

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
                grade = 0                
                for i in parts[1:]:
                    grade += int(i)
                my_dict[parts[0]] = grade
    return my_dict

def printout():
    zero = lis_of_num(0,15)
    one = lis_of_num(15, 18)
    two = lis_of_num(18, 21)
    three = lis_of_num(21, 24)
    four = lis_of_num(24, 28)

    points = my_iteration(my_points)                    #the number of exam points awarded
    name = one_iteration(student_info)                  #name
    exercises = my_iteration(exercise_data)             #The number of exercises completed
    print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")
    for key, value in name.items():
        final_points = int(exercises[key] / 40 * 10)    #the number of exercise points awarded
        result = points[key] + final_points        #the total number of points awarded
        if result in zero:                              #grade
            grade = 0
        elif result in one:
            grade = 1
        elif result in two:
            grade = 2
        elif result in three:
            grade = 3
        elif result in four:
            grade = 4
        else:
            grade = 5
        print(f"{(name[key][0] + " " + name[key][1]):29} {exercises[key]:<10}{final_points:<10}{points[key]:<10}{result:<10}{grade}")


printout()

