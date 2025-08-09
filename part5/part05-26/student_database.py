def add_student(students : dict, name : str):
    students[name] = []

def print_student(students : dict, name: str):
    if name in students and len(students[name]) > 0:
        print(name + ":")
        print(f" {len(students[name])} completed courses:")
        result = 0
        for i in students[name]:
            print(f"  {i[0]} {i[1]}")
            result += i[1]
        print(f" average grade {result/len(students[name])}")
    elif name in students and len(students[name]) == 0:
        print(name + ":")
        print(f" no completed courses")
    else:
        print(f"{name}: no such person in the database")

def add_course(students : dict, name: str, course : tuple):
    if course[1] != 0:
        for i in students[name]:
            if course[0] == i[0] and course[1] > i[1]:
                students[name].remove(i)
                students[name].append(course)
                return
            elif course[0] == i[0] and course[1] < i[1]:
                return
        students[name].append(course)


def summary(students : dict):
    print(f"students {len(students)}")
    most_courses(students)
    best_avg(students)

def most_courses(students):
    most_courses = 0
    person = ""
    for key, value in students.items():
        if len(students[key]) > most_courses:
            most_courses = len(students[key])
            person = key
    print(f"most courses completed {most_courses} {person}")

def best_avg(students):
    best_avg = 0
    name = ""
    result = 0
    for key, value in students.items():
        for i in students[key]:
            result += i[1]
        if result/len(students[key]) > best_avg:
            best_avg = result/len(students[key])
            name = key
        result = 0
    print(f"best average grade {best_avg} {name}")
        
        

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")
