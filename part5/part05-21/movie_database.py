def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    my_dict = {}
    my_dict["name"] = name
    my_dict["director"] = director
    my_dict["year"] = year
    my_dict["runtime"] = runtime
    database.append(my_dict)

    
    

if __name__ =="__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)