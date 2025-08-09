def line(a, b):
    if b == "":
        b = "*"
    print(a*b[0])


def square_of_hashes(size):
    for i in range(size):
        line(size, "#")




if __name__ == "__main__":
    square_of_hashes(5)
