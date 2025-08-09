def line(a, b):
    if b == "":
        b = "*"
    print(a*b[0])

def triangle(size):
    a = size - 1
    for i in range(size):
        line(size - a, "#")
        a -= 1
        




if __name__ == "__main__":
    triangle(3)
