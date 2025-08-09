def line(a, b):
    if b == "":
        b = "*"
    print(a*b[0])



def shape(a, b, c, d):
    x = a-1
    for i in range(a,):
        line(a - x, b)
        x -= 1
    for z in range(c):
        line(a, d)
        






if __name__ == "__main__":
    shape(5, "X", 3, "*")