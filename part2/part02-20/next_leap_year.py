year = int(input("Year: "))
year1 = year


while True:
    if year % 4 == 0:
        if (year + 4) % 100 == 0 and (year + 4) % 400 != 0:
            print(f"The next leap year after {year} is {year + 8}")
            break
        
        print(f"The next leap year after {year} is {year + 4}")
        break
    else:
        while not year % 4 == 0:
            year += 1
            if year % 100 == 0 and year % 400 != 0:
                year += 4

        print(f"The next leap year after {year1} is {year}")
        break


                





