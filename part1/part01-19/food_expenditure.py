cafe_meals = int(input())
lunch = float(input())
groceries = float(input())

daily = (cafe_meals * lunch + groceries)/7 
weekly = (cafe_meals * lunch + groceries)


print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")
