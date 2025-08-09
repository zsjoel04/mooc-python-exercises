hourly_w = float(input("Hourly wage: "))
hours_wkd = int(input("Hours worked: "))
day = input("Day of the week: ")
daily_w = hourly_w * hours_wkd
daily_w_sunday = daily_w * 2

if day =="Sunday":
    print (f"Daily wages: {daily_w_sunday} euros ")
else: 
    print (f"Daily wages: {daily_w} euros ")

