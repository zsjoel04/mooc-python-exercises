
def double_items(numbers: list[int]) -> list[int]:
    result = numbers[:]
    for i in range(len(numbers)):
        result[i] = numbers[i] * 2
    return result



if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)