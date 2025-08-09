def line(a, b):
    if b == "":
        b = "*"
    print(a*b[0])


def square(size, character):
    for i in range(size):
        line(size, character)




if __name__ == "__main__":
    square(5, "x")