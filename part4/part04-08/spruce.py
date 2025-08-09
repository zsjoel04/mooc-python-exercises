def spruce(a):
    print("a spruce!")
    x = a-1
    saved_x = x
    y = 1
    for i in range(a):
        print(" " * x + "*" * y)
        x -= 1
        y += 2
    print(" " * saved_x + "*" * 1)








if __name__ == "__main__":
    spruce(3)