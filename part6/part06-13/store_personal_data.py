def store_personal_data(person: tuple):    #("Paul Paulson", 37, 175.5)
    with open("people.csv", "a") as my_file:
        my_file.write(f"{person[0]};{person[1]};{person[2]}\n")



