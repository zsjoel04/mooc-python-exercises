def line(a, b):
    if b == "":
        b = "*"
    print(a*b[0])

# if __name__ == "__main__":
#     line(10, "#")


def box_of_hashes(height):
    for i in range(height):
        line(10, "#")




if __name__ == "__main__":
    box_of_hashes(5)
