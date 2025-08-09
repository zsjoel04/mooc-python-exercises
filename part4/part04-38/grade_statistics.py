
def asking_for_results():
    my_list = []
    data = input("Exam points and exercises completed: ")
    while True:
        if data == "":
            return my_list
        my_list.append(data)
        data = input("Exam points and exercises completed: ")

def convering_to_integers(list):
    collector_list = []
    mini_list = []
    for i in range(len(list)):
        find = list[i].find(" ")
        mini_list.append(int(list[i][:find]))
        mini_list.append(int(list[i][find + 1:]))
        collector_list.append(mini_list)
        mini_list = []
    return collector_list

#Innentol kezdodnek a segedfunkciok

def points_average(list):
    result = 0
    for i in range(len(list)):
        result += list[i][0] + int(list[i][1]/10)
    result = result / len(list)
    return result

def num_of_passing_students(list):
    passing_students = []
    for i in range(len(list)):
        if list[i][0] < 10:
            continue
        elif (list[i][0] + int(list[i][1]/10)) < 15:
            continue
        passing_students.append(list[i])
    return len(passing_students)

def pass_percentage(num1, num2):
    result = float((num2 / num1) * 100)
    return round(result, 1)


def grade_distribution(list):
    zero = 0
    zero_list = []
    for i in range(15):
        zero_list.append(i)
    one = 0
    one_list = [15, 16, 17]
    two = 0
    two_list = [18, 19, 20]
    three = 0
    three_list = [21, 22, 23]
    four = 0
    four_list = [24, 25, 26, 27]
    five = 0
    five_list = [28, 29, 30]
    for i in range(len(list)):
        result = list[i][0] + int(list[i][1]/10)
        if list[i][0] < 10:
            zero += 1
            continue
        if result in zero_list:
            zero += 1
        elif result in one_list:
            one += 1
        elif result in two_list:
            two += 1
        elif result in three_list:
            three += 1
        elif result in four_list:
            four += 1
        elif result in five_list:
            five += 1
    
    print(f"  5: {"*" * five}")
    print(f"  4: {"*" * four}")
    print(f"  3: {"*" * three}")
    print(f"  2: {"*" * two}")
    print(f"  1: {"*" * one}")
    print(f"  0: {"*" * zero}")





def main():
    a = asking_for_results()
    b = convering_to_integers(a)
    c = points_average(b)
    print("Statistics:")
    print(f"Points average: {c}")
    d = num_of_passing_students(b)
    e = pass_percentage(len(b), d)
    print(f"Pass percentage: {e}")
    print("Grade distribution: ")
    grade_distribution(b)
    

main()

# 10 85
# 15 54
# 20 0
# 5 100
# 11 45
# 16 45