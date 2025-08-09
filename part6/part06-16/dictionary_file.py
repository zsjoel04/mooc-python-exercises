def word_search():
    my_dict = {}
    with open("dictionary.txt") as new_file:
        for line in new_file:
            line = line.strip()
            dispose = line.split(" - ")
            my_dict[dispose[0]] = dispose[1]
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        my_input = input("Function")
        if my_input == "1":
            finn_word = input("The word in Finnish: ")
            english_word = input("The word in English: ")
            my_dict[finn_word] = english_word
            with open("dictionary.txt", "w") as append_to_file:
                for finn, english in my_dict.items():
                    append_to_file.write(f"{finn} - {english}\n")
            print("Dictionary entry added")
        elif my_input == "2":
            search_term = input("Search term: ")
            for finn, english in my_dict.items():
                result = []
                if search_term in finn or search_term in english:
                    result.append(f"{finn} - {english}")
                for i in result:
                    print(i)
        elif my_input == "3":
            print("Bye!")
            return

word_search()
#with open("dictionary.txt", "w") as append_to_file:
    # pass