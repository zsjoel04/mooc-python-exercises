def editor(editor):
    while True:        
        if editor.lower() == "visual studio code":
            print("an excellent choice!")
            break
        elif editor.lower() == "word" or editor.lower() == "notepad":
            print("awful")
            editor = input("Editor: ")
            continue
        else:
            print("not good")
            editor = input("Editor: ")
            continue
        
a = input("Editor: ")
editor(a)

