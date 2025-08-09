print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
if temp > 20:                                   # 21-
    if rain == "no":
        print("Wear jeans and a T-shirt")
    else:
        print("Wear jeans and a T-shirt")
        print("Don't forget your umbrella!")
if temp > 10 and temp <= 20:                       # 11-20
    if rain == "no":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
    else:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Don't forget your umbrella!")
if temp > 5 and temp <= 10:                        #6-10
    if rain == "no":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
    else:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Don't forget your umbrella!")
if temp < 6:                                        #0-5
    if rain == "yes":
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Make it a warm coat, actually")
        print("I think gloves are in order")
        print("Don't forget your umbrella!")
    else:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Make it a warm coat, actually")
        print("I think gloves are in order")
        
