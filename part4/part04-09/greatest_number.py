
def greatest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    elif a == b and a > c:
        return a
    elif a == c and a > b:
        return a
    elif b == c and b > a:
        return b
    else:
        return a






if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)


