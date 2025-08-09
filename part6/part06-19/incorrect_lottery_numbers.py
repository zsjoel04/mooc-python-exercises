def filter_incorrect():
    my_dict = {}
    correct_list = []
    allowed_nums = [num for num in range(1, 40)]
    with open("lottery_numbers.csv") as weeks:
        for week in weeks:
            week = week.strip()
            week_split = week.split(";")
            my_dict[week_split[0]] = week_split[1]
    for week, nums in my_dict.items():
        week_split = week.split(" ")
        nums_split = nums.split(",")
        # print(nums_split)
        # print(allowed_nums)
        week_num = week_split[1]
        try:
            check_week_num = int(week_num)
            check_nums_isdigit = [int(num) for num in nums_split]
            for num in nums_split:
                if not int(num) in allowed_nums:
                    raise ValueError
            if len(nums_split) != 7:
                raise ValueError
            if not len(nums_split) == len(set(nums_split)):
                raise ValueError
            correct_list.append(f"{week};{nums}\n")
        except ValueError:
            pass
    with open("correct_numbers.csv", "w") as correct_weeks:
        for week in correct_list:
            correct_weeks.write(week)
            
    
filter_incorrect()