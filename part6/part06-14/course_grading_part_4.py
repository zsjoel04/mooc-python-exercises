
if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    my_points = input("points: ")
    course_information = input("Course information:")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    my_points = "exam_points1.csv"
    course_information = "course1.txt"

def course_info(my_txt: str):
    res = []
    line_num = 1
    with open(my_txt) as my_file:
        for line in my_file:
            line = line.strip()
            parts = line.split()
            if line_num == 1:
                course_name = " ".join(parts[1:])
                res.append(course_name)
                line_num += 1
            else:
                credits = f"{parts[2]} credits"
                res.append(credits)
            
    return res
        



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
    course_name = course_info(course_information)[0]
    credits = course_info(course_information)[1]
    with open("results.csv", "w") as csv_file, open("results.txt", "w") as txt_file:
        txt_file.write(f"{course_name}, {credits}\n")
        txt_file.write("======================================\n")
        txt_file.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n")
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
            txt_file.write(f"{(name[key][0] + " " + name[key][1]):29} {exercises[key]:<10}{final_points:<10}{points[key]:<10}{result:<10}{grade}\n")
            csv_file.write(f"{key};{value[0]} {value[1]};{grade}\n")
        


printout()

if False:
    def clear(file):
        with open(file, "w") as my_file:
            pass
    clear("result.txt")
    clear("result.csv")