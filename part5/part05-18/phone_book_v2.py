def phonebook():
    my_dict = {}
    while True:
        my_input = input("command (1 search, 2 add, 3 quit): ")
        if my_input == "2":
            name = input("name: ")
            number = input("number: ")
            if not name in my_dict:
                my_dict[name] = []
            my_dict[name].append(number)    
            print("ok!")
        elif my_input == "1":
            name = input("name: ")
            if name in my_dict:
                for item in my_dict[name]:
                    print(item)
            else:
                print("no number")
        elif my_input == "3":
            print("quitting...")
            return   

phonebook()