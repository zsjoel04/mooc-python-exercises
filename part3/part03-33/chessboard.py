def chessboard(a):
    for i in range(a):
        if i % 2 == 0:
            for i in range(a):
                if i % 2 == 0:
                    print("1", end = "")
                else:
                    print("0", end = "")
        else:
            for i in range(a):
                if i % 2 == 0:
                    print("0", end = "")
                else:
                    print("1", end = "")
        print()

           




# Testing the function
if __name__ == "__main__":
    chessboard(3)
