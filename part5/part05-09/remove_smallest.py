def remove_smallest(numbers: list[int]) -> list[int]:
    # saved = numbers[0]
    # for number in numbers:
    #     if number < saved:
    #         saved = number
    numbers.remove(min(numbers))



if __name__ == "__main__":
    my_numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(my_numbers)
    print(my_numbers)