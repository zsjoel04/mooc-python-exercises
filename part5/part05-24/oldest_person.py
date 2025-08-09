def oldest_person(people: list):
    index = 1
    oldest = people[0][index]
    my_person = people[0][0]
    for person in range(len(people)):
        if people[person][index] < oldest:
            oldest = people[person][index]
            my_person = people[person][0]
    index -= 1
    oldest = people[person][index]
    return my_person
    

        


if __name__ =="__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [('Arthur', 1977), ('Emily', 2014)]

    print(oldest_person(people))