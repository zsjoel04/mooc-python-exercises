def read_input(command : str, num1 : int, num2 : int):
    while True:
        try:
            number = int(input(command))
            if number in range(num1, num2):
                return number
            else:
                print(f"You must type in an integer between {num1} and {num2}")
        except ValueError:
            print(f"You must type in an integer between {num1} and {num2}")

if __name__ == "__main__":
    number = read_input('Give a number', 95, 105)
    print("You typed in:", number)