
def largest():
    with open("numbers.txt") as buzi:
        largest = 0
        for num in buzi:
            if int(num) > largest:
                largest = int(num)
    return(largest)

